import pytest

from day04 import Elf, Pair, do_assignments_fully_overlap, set_up_pairs


@pytest.mark.parametrize(
    "pair,expected_outcome",
    [
        (Pair(Elf(2, 4), Elf(6, 8)), False),
        (Pair(Elf(2, 3), Elf(4, 5)), False),
        (Pair(Elf(5, 7), Elf(7, 9)), False),
        (Pair(Elf(2, 8), Elf(3, 7)), True),
        (Pair(Elf(6, 6), Elf(4, 6)), True),
        (Pair(Elf(2, 6), Elf(4, 8)), False),
    ],
)
def test_do_assignments_fully_overlap(pair: Pair, expected_outcome: bool) -> None:
    overlap = do_assignments_fully_overlap(pair)

    assert overlap == expected_outcome, "You messed up calculating the overlap somehow."


def test_creating_pairings_from_input() -> None:
    expected_pairings = (
        Pair(Elf(2, 4), Elf(6, 8)),
        Pair(Elf(2, 3), Elf(4, 5)),
        Pair(Elf(5, 7), Elf(7, 9)),
        Pair(Elf(2, 8), Elf(3, 7)),
        Pair(Elf(6, 6), Elf(4, 6)),
        Pair(Elf(2, 6), Elf(4, 8)),
    )

    generated_pairings = set_up_pairs("inputs/day04_sample.txt")

    assert generated_pairings == expected_pairings, "The pairings are wrong."
