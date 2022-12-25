from pathlib import Path
import enum


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
