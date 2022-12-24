from functools import partial
import pytest

from day08 import (
    Map,
    number_of_visible_trees_from_outside,
    read_map,
    visible_trees_from_outside,
)


@pytest.fixture
def sample_map() -> Map:
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def sample_visibility() -> Map:
    return [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],  # left+top, right+top, not
        [1, 1, 0, 1, 1],  # right, not, right
        [1, 0, 1, 0, 1],  # not, left_bottom, not
        [1, 1, 1, 1, 1],
    ]


def test_read_map(sample_map) -> None:
    assert read_map("inputs/day08_sample.txt") == sample_map


def test_number_of_visible_trees_from_outside(sample_map) -> None:
    assert number_of_visible_trees_from_outside(sample_map) == 21


def test_visible_trees_from_outside(sample_map, sample_visibility):
    assert visible_trees_from_outside(sample_map) == sample_visibility
