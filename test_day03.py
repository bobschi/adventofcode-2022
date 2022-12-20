import pytest

from day03 import (
    Group,
    Rucksack,
    calculate_item_priority,
    create_groups_from_rucksacks,
    create_rucksacks_from_packing_lists,
    find_shared_item_type,
    get_group_badge,
    pack_into_rucksack,
)


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
def test_find_shared_item_type(contents: str, expected_shared_type: str):
    packed_rucksack = pack_into_rucksack(contents)
    shared_type = find_shared_item_type(packed_rucksack)

    assert shared_type == expected_shared_type, "You found the wrong shared type."


@pytest.mark.parametrize(
    "contents,expected_priority",
    [("pp", 16), ("LL", 38), ("PP", 42), ("vv", 22), ("tt", 20), ("ss", 19)],
)
def test_calculate_shared_item_priority(contents: str, expected_priority: int):
    packed_rucksack = pack_into_rucksack(contents)
    calculated_priority = calculate_item_priority(packed_rucksack)

    assert calculated_priority == expected_priority, (
        "Either you are finding the wrong shared item -- Are other tests failing? -- or"
        "you are assigning the wrong priority."
    )


def test_create_rucksacks_from_input():
    path_to_packing_lists = "inputs/day03_sample.txt"
    expected_rucksacks = (
        pack_into_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"),
        pack_into_rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
        pack_into_rucksack("PmmdzqPrVvPwwTWBwg"),
        pack_into_rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
        pack_into_rucksack("ttgJtRGJQctTZtZT"),
        pack_into_rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"),
    )

    rucksacks = create_rucksacks_from_packing_lists(path_to_packing_lists)

    assert len(rucksacks) == len(
        expected_rucksacks
    ), "You are either packing too many or too few rucksacks."
    assert (
        expected_rucksacks == rucksacks
    ), "Your rucksacks don't hold the expected contents."


def test_create_groups_from_input():
    path_to_packing_lists = "inputs/day03_sample.txt"
    expected_groups = (
        Group(
            elf_one=pack_into_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"),
            elf_two=pack_into_rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
            elf_three=pack_into_rucksack("PmmdzqPrVvPwwTWBwg"),
        ),
        Group(
            elf_one=pack_into_rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
            elf_two=pack_into_rucksack("ttgJtRGJQctTZtZT"),
            elf_three=pack_into_rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"),
        ),
    )

    groups = create_groups_from_rucksacks(path_to_packing_lists)

    assert len(groups) == len(
        expected_groups
    ), "You are either making too many or too few groups."


@pytest.mark.parametrize(
    "group,expected_badge",
    [
        (
            Group(
                elf_one=pack_into_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"),
                elf_two=pack_into_rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
                elf_three=pack_into_rucksack("PmmdzqPrVvPwwTWBwg"),
            ),
            "r",
        ),
        (
            Group(
                elf_one=pack_into_rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
                elf_two=pack_into_rucksack("ttgJtRGJQctTZtZT"),
                elf_three=pack_into_rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"),
            ),
            "Z",
        ),
    ],
)
def test_get_group_badge(group: Group, expected_badge: str):
    badge = get_group_badge(group)

    assert badge == expected_badge, "You messed up calculating the group badge somehow."
