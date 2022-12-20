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
