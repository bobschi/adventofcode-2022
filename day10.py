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


def calculate_display_contents(register_states: list[int]) -> list[str]:
    pixels: list[str] = ["."] * 240
    for position, register_state in enumerate(register_states[1:]):
        if position % 40 in [register_state - 1, register_state, register_state + 1]:
            pixels[position] = "#"

    display_content: list[str] = []
    for start in range(0, 240, 40):
        display_content.append("".join(pixels[start : start + 40]))

    return display_content


def solve_part_two() -> None:
    commands = get_data(AOC_SESSION, DAY, YEAR).splitlines()
    register_states = execute(commands)
    display_content = calculate_display_contents(register_states)

    print("\n".join(display_content))


if __name__ == "__main__":
    solve_part_two()
