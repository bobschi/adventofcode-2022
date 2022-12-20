import pytest

from day06 import find_start_of_message_marker, find_start_of_packet_marker


@pytest.mark.parametrize(
    "datastream,expected_index",
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ),
)
def test_find_marker(datastream: str, expected_index: int):
    index = find_start_of_packet_marker(datastream)

    assert index == expected_index


@pytest.mark.parametrize(
    "datastream,expected_index",
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ),
)
def test_find_start_of_message_marker(datastream: str, expected_index: int):
    index = find_start_of_message_marker(datastream)

    assert index == expected_index
