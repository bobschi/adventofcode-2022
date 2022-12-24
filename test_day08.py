from functools import partial
import pytest

from day08 import Map, number_of_visible_trees_from_outside, read_map


@pytest.fixture
def sample_map() -> Map:
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def test_read_map(sample_map) -> None:
    assert read_map("inputs/day08_sample.txt") == sample_map


def test_solve_part_one(sample_map) -> None:
    assert number_of_visible_trees_from_outside(sample_map) == 21
