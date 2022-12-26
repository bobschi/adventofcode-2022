import pytest

from day09 import Direction, Command, Rope, RopeEnd, execute_commands, read_commands


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


@pytest.fixture
def head() -> RopeEnd:
    return RopeEnd()


@pytest.fixture
def tail() -> RopeEnd:
    return RopeEnd()


def test_read_commands(sample_command_list: list[Command]) -> None:
    command_list = read_commands("inputs/day09_sample.txt")
    assert command_list == sample_command_list


def test_move_rope_end(head: RopeEnd) -> None:
    head = head.move(Direction.LEFT)
    assert head == RopeEnd(-1, 0)

    head = head.move(Direction.UP)
    assert head == RopeEnd(-1, 1)

    head = head.move(Direction.RIGHT)
    assert head == RopeEnd(0, 1)

    head = head.move(Direction.DOWN)
    assert head == RopeEnd()


@pytest.mark.parametrize(
    "rope_end,expected_sign",
    [
        [RopeEnd(10, 9), RopeEnd(1, 1)],
        [RopeEnd(-8, 7), RopeEnd(-1, 1)],
        [RopeEnd(5, -3), RopeEnd(1, -1)],
        [RopeEnd(-2, -4), RopeEnd(-1, -1)],
        [RopeEnd(-1, -1), RopeEnd(-1, -1)],
        [RopeEnd(0, 0), RopeEnd(0, 0)],
    ],
)
def test_sign(rope_end: RopeEnd, expected_sign: RopeEnd):
    assert rope_end.sign() == expected_sign


@pytest.mark.parametrize(
    "direction,end_position",
    [
        [Direction.LEFT, RopeEnd(-1, 0)],
        [Direction.UP, RopeEnd(0, 1)],
        [Direction.RIGHT, RopeEnd(1, 0)],
        [Direction.DOWN, RopeEnd(0, -1)],
    ],
)
def test_follow_other_end_on_axis(
    head: RopeEnd, tail: RopeEnd, direction: Direction, end_position: RopeEnd
) -> None:
    head = head.move(direction)
    tail = tail.follow(head)

    assert tail == RopeEnd()

    head = head.move(direction)
    tail = tail.follow(head)

    assert tail == end_position


@pytest.mark.parametrize(
    "directions,end_position",
    [
        [[Direction.RIGHT, Direction.UP, Direction.UP], RopeEnd(1, 1)],
        [[Direction.LEFT, Direction.UP, Direction.UP], RopeEnd(-1, 1)],
        [[Direction.RIGHT, Direction.DOWN, Direction.DOWN], RopeEnd(1, -1)],
        [[Direction.LEFT, Direction.DOWN, Direction.DOWN], RopeEnd(-1, -1)],
    ],
)
def test_follow_other_end_on_diagonals(
    head: RopeEnd, tail: RopeEnd, directions: list[Direction], end_position: RopeEnd
) -> None:
    for direction in directions:
        head = head.move(direction)
        tail = tail.follow(head)

    assert tail == end_position


@pytest.mark.parametrize(
    "directions,end_result",
    [
        [
            [Direction.LEFT, Direction.LEFT],
            Rope(RopeEnd(-2, 0), RopeEnd(-1, 0)),
        ],
        [
            [Direction.UP, Direction.UP],
            Rope(RopeEnd(0, 2), RopeEnd(0, 1)),
        ],
        [
            [Direction.RIGHT, Direction.RIGHT],
            Rope(RopeEnd(2, 0), RopeEnd(1, 0)),
        ],
        [
            [Direction.DOWN, Direction.DOWN],
            Rope(RopeEnd(0, -2), RopeEnd(0, -1)),
        ],
        [
            [Direction.RIGHT, Direction.UP, Direction.UP],
            Rope(RopeEnd(1, 2), RopeEnd(1, 1)),
        ],
        [
            [Direction.LEFT, Direction.UP, Direction.UP],
            Rope(RopeEnd(-1, 2), RopeEnd(-1, 1)),
        ],
        [
            [Direction.DOWN, Direction.RIGHT, Direction.DOWN],
            Rope(RopeEnd(1, -2), RopeEnd(1, -1)),
        ],
        [
            [Direction.DOWN, Direction.LEFT, Direction.DOWN],
            Rope(RopeEnd(-1, -2), RopeEnd(-1, -1)),
        ],
        [
            [Direction.LEFT, Direction.UP, Direction.LEFT],
            Rope(RopeEnd(-2, 1), RopeEnd(-1, 1)),
        ],
        [
            [Direction.LEFT, Direction.DOWN, Direction.LEFT],
            Rope(RopeEnd(-2, -1), RopeEnd(-1, -1)),
        ],
        [
            [Direction.RIGHT, Direction.UP, Direction.RIGHT],
            Rope(RopeEnd(2, 1), RopeEnd(1, 1)),
        ],
        [
            [Direction.RIGHT, Direction.DOWN, Direction.RIGHT],
            Rope(RopeEnd(2, -1), RopeEnd(1, -1)),
        ],
    ],
)
def test_rope(directions: list[Direction], end_result: Rope) -> None:
    rope = Rope()
    print(rope)

    for direction in directions:
        rope = rope.move_head(direction)
        print(rope)

    assert rope == end_result
    print()


def test_execute_commands(sample_command_list: list[Command]) -> None:
    visited = execute_commands(sample_command_list)

    assert len(visited) == 13
