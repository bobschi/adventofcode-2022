from functools import partial
import pytest

from day08 import Direction, Map, visible_trees_in_line


@pytest.fixture
def asymmetric() -> Map:
    return [
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
    ]


@pytest.fixture
def ring_of_trees() -> Map:
    return [
        [1, 2, 1],
        [2, 0, 2],
        [1, 2, 3],
    ]


def test_number_of_visible_trees_asymmetric_map_left(asymmetric) -> None:
    visible_left = partial(visible_trees_in_line, asymmetric, Direction.LEFT)

    assert visible_left(0) == 1
    assert visible_left(1) == 1
    assert visible_left(2) == 1


def test_number_of_visible_trees_ring_of_trees_left(ring_of_trees) -> None:
    visible_left = partial(visible_trees_in_line, ring_of_trees, Direction.LEFT)

    assert visible_left(0) == 2
    assert visible_left(1) == 1
    assert visible_left(2) == 3


def test_number_of_visible_trees_asymmetric_map_right(asymmetric) -> None:
    visible_right = partial(visible_trees_in_line, asymmetric, Direction.RIGHT)

    assert visible_right(0) == 1
    assert visible_right(1) == 1
    assert visible_right(2) == 1


def test_number_of_visible_trees_ring_of_trees_right(ring_of_trees) -> None:
    visible_right = partial(visible_trees_in_line, ring_of_trees, Direction.RIGHT)

    assert visible_right(0) == 2
    assert visible_right(1) == 1
    assert visible_right(2) == 1


def test_number_of_visible_trees_asymmetric_map_down(asymmetric) -> None:
    visible_down = partial(visible_trees_in_line, asymmetric, Direction.DOWN)

    assert visible_down(0) == 0
    assert visible_down(1) == 1
    assert visible_down(2) == 0
    assert visible_down(3) == 1


def test_number_of_visible_trees_ring_of_trees_down(ring_of_trees) -> None:
    visible_down = partial(visible_trees_in_line, ring_of_trees, Direction.DOWN)

    assert visible_down(0) == 2
    assert visible_down(1) == 1
    assert visible_down(2) == 3


def test_number_of_visible_trees_asymmetric_map_up(asymmetric) -> None:
    visible_up = partial(visible_trees_in_line, asymmetric, Direction.UP)

    assert visible_up(0) == 0
    assert visible_up(1) == 1
    assert visible_up(2) == 0
    assert visible_up(3) == 1


def test_number_of_visible_trees_ring_of_trees_up(ring_of_trees) -> None:
    visible_up = partial(visible_trees_in_line, ring_of_trees, Direction.UP)

    assert visible_up(0) == 2
    assert visible_up(1) == 1
    assert visible_up(2) == 1
