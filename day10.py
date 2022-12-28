from aocd import get_data, submit

DAY = 10
YEAR = 2022
AOC_SESSION = open(".aoc-token").read().strip()


def execute(commands: list[str]) -> list[int]:
    register_x: int = 1
    register_states = [1]

    def execute_command(x: int, command: str) -> int:
        match command.split():
            case ["noop"]:
                register_states.append(x)
            case ["addx", number]:
                register_states.extend([x, x])
                x += int(number)

        return x

    for command in commands:
        register_x = execute_command(register_x, command)

    return register_states


def solve_part_one() -> None:
    commands = get_data(AOC_SESSION, DAY, YEAR).splitlines()

    register_states = execute(commands)
    signal_strengths = [register_states[index] * index for index in range(20, 260, 40)]
    solution_part_one = sum(signal_strengths)

    submit(answer=solution_part_one, part="a", day=DAY, year=YEAR, session=AOC_SESSION)


if __name__ == "__main__":
    solve_part_one()
