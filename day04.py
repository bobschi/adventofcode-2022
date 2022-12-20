from dataclasses import dataclass


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


def do_assigments_fully_overlap(elf_a: Elf, elf_b: Elf) -> bool:
    """
    Return True if one assigment is fully contained in the other, False if not.
    """
    return (
        elf_a.get_assignment() <= elf_b.get_assignment()
        or elf_b.get_assignment() <= elf_a.get_assignment()
    )
