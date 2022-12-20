from functools import partial


def find_marker(marker_size: int, datastream: str) -> int:
    """
    Return the last character index of the first group of four distinct characters.
    """
    for i in range(len(datastream) - marker_size - 1):
        current_sequence = set(datastream[i : i + marker_size])
        if len(current_sequence) == marker_size:
            return i + marker_size

    return -1


find_start_of_packet_marker = partial(find_marker, 4)
find_start_of_message_marker = partial(find_marker, 14)


if __name__ == "__main__":
    with open("inputs/day06.txt") as file:
        datastream = file.read()

    print(f"The solution for part one is {find_start_of_packet_marker(datastream)}")
    print(f"The solution for part one is {find_start_of_message_marker(datastream)}")
