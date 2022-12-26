import enum
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self


class Direction(enum.StrEnum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


Command = tuple[Direction, int]


def read_commands(command_file_path: Path) -> list[Command]:
    with open(command_file_path, "r") as command_file:
        commands = command_file.readlines()

    command_list = []
    for command in commands:
        direction, amount = command.split()
        command_list.append((Direction(direction), int(amount)))

    return command_list


@dataclass
class RopeEnd:
    x: int = 0
    y: int = 0

    def move(self, direction: Direction) -> Self:
        match direction:
            case Direction.LEFT:
                return self + RopeEnd(-1, 0)
            case Direction.UP:
                return self + RopeEnd(0, 1)
            case Direction.RIGHT:
                return self + RopeEnd(1, 0)
            case Direction.DOWN:
                return self + RopeEnd(0, -1)

    def sign(self) -> Self:
        def _sign(number: int) -> int:
            if number == 0:
                return 0
            return int(math.copysign(1, number))

        return RopeEnd(_sign(self.x), _sign(self.y))

    def follow(self, other: Self) -> Self:
        difference = other - self

        if difference == difference.sign():
            return self

        return self + difference.sign()

    def __add__(self, other: Self) -> Self:
        return RopeEnd(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return RopeEnd(self.x - other.x, self.y - other.y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x + self.y))


@dataclass(frozen=True)
class Rope:
    head: RopeEnd = field(default_factory=RopeEnd)
    tail: RopeEnd = field(default_factory=RopeEnd)

    def move_head(self, direction: Direction) -> Self:
        new_head = self.head.move(direction)
        new_tail = self.tail.follow(new_head)

        return Rope(new_head, new_tail)

    def __eq__(self, other: Self) -> bool:
        return self.head == other.head and self.tail == other.tail


def execute_commands(commands: list[Command]) -> set[RopeEnd]:
    rope = Rope()
    visited = set()

    for command in commands:
        for _ in range(command[1]):
            rope = rope.move_head(command[0])
            visited.add(rope.tail)

    return visited


def solve_part_one() -> None:
    commands = read_commands("inputs/day09_input.txt")
    visited = execute_commands(commands)

    print(f"The solution for part one is {len(visited)}")


@dataclass(frozen=True)
class TenKnotRope:
    knots: list[RopeEnd] = field(default_factory=list)

    def __init__(self) -> Self:
        self.knots = [[RopeEnd()] * 10]

    @property
    def head(self) -> RopeEnd:
        return self.knots[0]

    @property
    def tail(self) -> RopeEnd:
        return self.knots[-1]

    def move_head(self, direction: Direction) -> Self:
        new_knots = [self.head.move(direction)]
        for index, knot in enumerate(self.knots[1:]):
            new_knots.append(knot.follow(new_knots[index]))

        return TenKnotRope(knots=new_knots)


def solve_part_one() -> None:
    commands = read_commands("inputs/day09_input.txt")
    visited = execute_commands(commands)

    print(f"The solution for part two is {len(visited)}")


if __name__ == "__main__":
    solve_part_one()
