from dataclasses import dataclass, field
from pathlib import Path
from typing import Self


@dataclass
class Directory:
    up: Self | None = None
    name: str = "/"
    subdirectories: list[Self] = field(default_factory=list)
    files: dict[str, int] = field(default_factory=dict)


def directory_name_with_path(cwd: Directory):
    path = []

    while cwd.up:
        path.append(f"{cwd.name}")
        cwd = cwd.up

    path.append("")
    path.reverse()

    return "/".join(path)


def calculate_directory_sizes(directory: Directory, size_cache: dict[str, int]) -> int:
    if directory.subdirectories == {}:
        return sum(directory.files.values())

    subdirectory_sizes: list[int] = []
    for subdirectory in directory.subdirectories:
        full_path = directory_name_with_path(subdirectory)
        size = calculate_directory_sizes(subdirectory, size_cache)

        size_cache[full_path] = size
        subdirectory_sizes.append(size)

    total_size = sum(directory.files.values()) + sum(subdirectory_sizes)

    if not directory.up:
        size_cache["/"] = total_size

    return total_size


def calculate_potential_savings(
    size_cache: dict[str, int], max_size: int = 100000
) -> int:
    return sum([size for size in size_cache.values() if size <= max_size])


def parse_line(line: str, cwd: Directory | None) -> Directory:
    match line.split():
        case ["$", "ls"]:
            pass

        case ["$", "cd", "/"]:
            pass

        case ["$", "cd", ".."]:
            cwd = cwd.up

        case ["$", "cd", name]:
            cwd = new_dir = Directory(cwd, name)
            cwd.up.subdirectories.append(new_dir)

        case ["dir", _]:
            pass

        case [size, name]:
            cwd.files[name] = int(size)

    return cwd


def parse_log(log_file: Path) -> Directory:
    cwd = root = Directory()

    with open(log_file) as console_log:
        log_lines = console_log.readlines()

    for line in log_lines:
        cwd = parse_line(line, cwd)

    return root


def print_file_tree(dir: Directory, level: int = 0) -> None:
    if level == 0:
        print("- / (dir)")

    indent = level * 2 * " "

    for subdirectory in dir.subdirectories:
        print(f"{indent}- {subdirectory.name} (dir)")
        print_file_tree(subdirectory, level + 1)

    for file_name, file_size in dir.files.items():
        print(f"{indent}- {file_name} (file, size={file_size})")


def print_directory_sizes(size_cache: dict[str, int]) -> None:
    for directory_full_name, size in size_cache.items():
        print(f"{directory_full_name} {size}")


def parse_sample_file() -> None:
    root = parse_log("inputs/day07_sample.txt")
    size_cache = {}

    print_file_tree(root)
    print()

    calculate_directory_sizes(root, size_cache)
    print_directory_sizes(size_cache)
    print()

    print(f"Solution for example is {calculate_potential_savings(size_cache)}")


def solve_part_one() -> dict[str, int]:
    root = parse_log("inputs/day07_input.txt")
    size_cache = {}

    calculate_directory_sizes(root, size_cache)

    print(f"Solution for part one is {calculate_potential_savings(size_cache)}")

    return size_cache


def solve_part_two(size_cache: dict[str, int]) -> None:
    total_disk_space = 70000000
    minimum_required_space = 30000000

    used_space = size_cache["/"]
    unused_space = total_disk_space - used_space
    required_space = minimum_required_space - unused_space

    solution = min([size for size in size_cache.values() if size >= required_space])
    print(f"Solution for part two is {solution}")


if __name__ == "__main__":
    parse_sample_file()

    print()

    size_cache = solve_part_one()
    solve_part_two(size_cache)
