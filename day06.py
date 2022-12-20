def find_marker(datastream: str) -> int:
    """
    Return the last character index of the first group of four distinct characters.
    """
    for i in range(len(datastream) - 3):
        current_sequence = set(datastream[i : i + 4])
        if len(current_sequence) == 4:
            return i + 4

    return -1


def solve_part_one() -> None:
    with open("inputs/day06.txt") as file:
        datastream = file.read()

    index = find_marker(datastream)

    print(f"The solution for part one is {index}")


if __name__ == "__main__":
    solve_part_one()
