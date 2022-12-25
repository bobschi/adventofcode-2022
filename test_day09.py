import pytest

from day09 import Direction, Command, RopeEnd, read_commands


@pytest.fixture
def sample_command_list() -> list[Command]:
    return [
        (Direction.RIGHT, 4),
        (Direction.UP, 4),
        (Direction.LEFT, 3),
        (Direction.DOWN, 1),
        (Direction.RIGHT, 4),
        (Direction.DOWN, 1),
        (Direction.LEFT, 5),
        (Direction.RIGHT, 2),
    ]


def test_read_commands(sample_command_list: list[Command]) -> None:
    command_list = read_commands("inputs/day09_sample.txt")
    assert command_list == sample_command_list


def test_move_rope_end() -> None:
    head = RopeEnd()

    head = head.move(Direction.LEFT)
    assert head == RopeEnd(-1, 0)

    head = head.move(Direction.UP)
    assert head == RopeEnd(-1, 1)

    head = head.move(Direction.RIGHT)
    assert head == RopeEnd(0, 1)

    head = head.move(Direction.DOWN)
    assert head == RopeEnd()
