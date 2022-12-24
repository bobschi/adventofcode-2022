from pathlib import Path


Map = list[list[int]]


def visible_trees_from_outside(map: Map) -> int:
    ...


def read_map(path_to_map: Path) -> Map:
    with open(path_to_map, "r") as map_file:
        map_contents = map_file.readlines()

    return [[int(height) for height in list(line.strip())] for line in map_contents]


def solve_part_one() -> None:
    map = read_map("inputs/day08_input.py")
    visible_trees = visible_trees_from_outside(map)

    print(f"The solution to part one is {visible_trees}")
