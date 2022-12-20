import pytest

from day04 import Elf, do_assigments_fully_overlap


@pytest.mark.parametrize(
    "elf_a,elf_b,expected_outcome",
    [
        (Elf(2, 4), Elf(6, 8), False),
        (Elf(2, 3), Elf(4, 5), False),
        (Elf(5, 7), Elf(7, 9), False),
        (Elf(2, 8), Elf(3, 7), True),
        (Elf(6, 6), Elf(4, 6), True),
        (Elf(2, 6), Elf(4, 8), False),
    ],
)
def test_do_assignments_fully_overlap(
    elf_a: set[int], elf_b: set[int], expected_outcome: bool
) -> None:
    overlap = do_assigments_fully_overlap(elf_a, elf_b)

    assert overlap == expected_outcome, "You messed up calculating the overlap somehow."