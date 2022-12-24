import pytest

from pytest_lazyfixture import lazy_fixture
from day08 import (
    Direction,
    Map,
    number_of_visible_trees_in_column,
    number_of_visible_trees_in_row,
)


@pytest.fixture
def one_tree_center() -> Map:
    return [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]


@pytest.fixture
def ring_of_trees() -> Map:
    return [
        [1, 2, 1],
        [2, 0, 2],
        [1, 2, 3],
    ]


@pytest.fixture
def sample_map() -> Map:
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


@pytest.mark.parametrize(
    "map,row,expected_number_of_trees",
    [
        [lazy_fixture("one_tree_center"), 0, (0, 0)],
        [lazy_fixture("one_tree_center"), 1, (1, 1)],
        [lazy_fixture("one_tree_center"), 2, (0, 0)],
        [lazy_fixture("ring_of_trees"), 0, (2, 2)],
        [lazy_fixture("ring_of_trees"), 1, (1, 1)],
        [lazy_fixture("ring_of_trees"), 2, (3, 1)],
        [lazy_fixture("sample_map"), 0, (2, 2)],
        [lazy_fixture("sample_map"), 1, (2, 2)],
        [lazy_fixture("sample_map"), 2, (1, 4)],
        [lazy_fixture("sample_map"), 3, (3, 1)],
        [lazy_fixture("sample_map"), 4, (3, 1)],
    ],
)
def test_number_of_visible_trees_in_row(
    map: Map, row: int, expected_number_of_trees: tuple[int, int]
) -> None:
    visible_left = number_of_visible_trees_in_row(row, Direction.LEFT, map)
    visible_right = number_of_visible_trees_in_row(row, Direction.RIGHT, map)

    assert visible_left == expected_number_of_trees[Direction.LEFT]
    assert visible_right == expected_number_of_trees[Direction.RIGHT]


@pytest.mark.parametrize(
    "map,column,expected_number_of_trees",
    [
        [lazy_fixture("one_tree_center"), 0, (0, 0)],
        [lazy_fixture("one_tree_center"), 1, (1, 1)],
        [lazy_fixture("one_tree_center"), 2, (0, 0)],
        [lazy_fixture("ring_of_trees"), 0, (2, 2)],
        [lazy_fixture("ring_of_trees"), 1, (1, 1)],
        [lazy_fixture("ring_of_trees"), 2, (3, 1)],
        [lazy_fixture("sample_map"), 0, (2, 2)],
        [lazy_fixture("sample_map"), 1, (2, 2)],
        [lazy_fixture("sample_map"), 2, (1, 4)],
        [lazy_fixture("sample_map"), 3, (3, 1)],
        [lazy_fixture("sample_map"), 4, (3, 1)],
    ],
)
def test_number_of_visible_trees_in_colum(
    map: Map, column: int, expected_number_of_trees: tuple[int, int]
) -> None:
    visible_down = number_of_visible_trees_in_column(column, Direction.DOWN, map)
    visible_down = number_of_visible_trees_in_column(column, Direction.UP, map)

    assert visible_down == expected_number_of_trees[Direction.DOWN]
    assert visible_down == expected_number_of_trees[Direction.UP]
