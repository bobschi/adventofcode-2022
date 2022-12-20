from dataclasses import dataclass


def do_assigments_fully_overlap(assignment_a: set[int], assignment_b: set[int]) -> bool:
    """
    Return True if one assigment is fully contained in the other, False if not.
    """
    return assignment_a <= assignment_b or assignment_b <= assignment_a


@dataclass
class Elf:
    assignment_start: int
    assignment_end: int

    def get_assignment(self) -> set[int]:
        return set(range(self.assignment_start, self.assignment_end))
