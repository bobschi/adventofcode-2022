from day03 import pack_into_rucksack, Rucksack
import pytest


@pytest.mark.parametrize(
    "contents,expected_compartment_one,expected_compartment_two",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrVvPwwTWBwg", "PmmdzqPrV", "vPwwTWBwg"),
    ],
)
def test_pack_into_rucksack(
    contents: str, expected_compartment_one: str, expected_compartment_two: str
):
    expected_rucksack = Rucksack(
        compartment_one=expected_compartment_one,
        compartment_two=expected_compartment_two,
    )

    packed_rucksack = pack_into_rucksack(contents)

    assert packed_rucksack == expected_rucksack, "You messed up packing your rucksack."


@pytest.mark.parametrize(
    "contents,expected_shared_type",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_shared_item_type(contents: str, expected_shared_type: str):
    packed_rucksack = pack_into_rucksack(contents)
    shared_type = packed_rucksack.shared_item_type

    assert shared_type == expected_shared_type, "You found the wrong shared type."
