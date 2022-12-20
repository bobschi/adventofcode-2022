import pytest
from day04 import do_assigments_fully_overlap


@pytest.mark.parametrize(
    "assignment_a,assignment_b,expected_outcome",
    [
        (set(range(2, 4)), set(range(6, 8)), False),
        (set(range(2, 3)), set(range(4, 5)), False),
        (set(range(5, 7)), set(range(7, 9)), False),
        (set(range(2, 8)), set(range(3, 7)), True),
        (set(range(6, 6)), set(range(4, 6)), True),
        (set(range(2, 6)), set(range(4, 8)), False),
    ],
)
def test_do_assignments_fully_overlap(
    assignment_a: set[int], assignment_b: set[int], expected_outcome: bool
) -> None:
    overlap = do_assigments_fully_overlap(assignment_a, assignment_b)

    assert overlap == expected_outcome, "You messed up calculating the overlap somehow."
