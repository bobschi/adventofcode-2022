from dataclasses import dataclass
from pathlib import Path


@dataclass
class Elf:
    assignment_start: int
    assignment_end: int

    def get_assignment(self) -> set[int]:
        return set(range(self.assignment_start, self.assignment_end))


@dataclass
class Pair:
    elf_a: Elf
    elf_b: Elf


def do_assignments_fully_overlap(pair: Pair) -> bool:
    """
    Return True if one assigment is fully contained in the other, False if not.
    """
    elf_a, elf_b = pair.elf_a, pair.elf_b

    return (
        elf_a.get_assignment() <= elf_b.get_assignment()
        or elf_b.get_assignment() <= elf_a.get_assignment()
    )


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
