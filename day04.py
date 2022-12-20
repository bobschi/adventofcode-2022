from dataclasses import dataclass
from pathlib import Path


@dataclass
class Elf:
    assignment_start: int
    assignment_end: int

    def get_assignment(self) -> set[int]:
        return set(range(self.assignment_start, self.assignment_end + 1))


@dataclass
class Pair:
    elf_a: Elf
    elf_b: Elf


def do_assignments_fully_overlap(pair: Pair) -> bool:
    """
    Return True if one assigment is fully contained in the other, False if not.
    """
    elf_a_assignment, elf_b_assignment = (
        pair.elf_a.get_assignment(),
        pair.elf_b.get_assignment(),
    )

    return elf_a_assignment <= elf_b_assignment or elf_b_assignment <= elf_a_assignment


def set_up_pairs(path_to_pair_list: Path) -> tuple[Pair]:
    """
    Return a list of pairs of elves generated from a correctly formatted input file.
    """
    with open(path_to_pair_list) as pair_list_file:
        pair_list = pair_list_file.read()

    def create_elf(range_string: str) -> Elf:
        assigment_range = range_string.split("-")
        assignment_start, assigment_end = map(int, assigment_range)
        return Elf(assignment_start, assigment_end)

    pairs = []
    for pairing in pair_list.splitlines():
        elf_a_range, elf_b_range = pairing.split(",")
        pairs.append(Pair(create_elf(elf_a_range), create_elf(elf_b_range)))

    return tuple(pairs)


def do_assigments_overlap(pair: Pair) -> bool:
    """
    Return True if assigned ranges overlap at least partially.
    """
    return not pair.elf_a.get_assignment().isdisjoint(pair.elf_b.get_assignment())


def solve_part_one() -> None:
    pairs = set_up_pairs("inputs/day04_input.txt")
    total_overlaps = len(tuple(filter(do_assignments_fully_overlap, pairs)))

    print(f"The solution for part one is {total_overlaps}")


if __name__ == "__main__":
    solve_part_one()
