def find_first_marker(datastream: str) -> int:
    """
    Return the last character index of the first group of four distinct characters.
    """
    for i in range(len(datastream) - 3):
        current_sequence = set(datastream[i : i + 4])
        if len(current_sequence) == 4:
            return i + 4

    return -1
