from dataclasses import dataclass
from functools import singledispatch
from pathlib import Path


@dataclass(frozen=True)
class Rucksack:
    compartment_one: str
    compartment_two: str

    @property
    def contents(self) -> str:
        return f"{self.compartment_one}{self.compartment_two}"


def pack_into_rucksack(contents: str) -> Rucksack:
    length = len(contents)
    return Rucksack(
        compartment_one=contents[: length // 2],
        compartment_two=contents[length // 2 :],
    )


def find_shared_item_type(rucksack: Rucksack) -> str:
    return (set(rucksack.compartment_one) & set(rucksack.compartment_two)).pop()


@singledispatch
def calculate_item_priority(item) -> int:
    pass


@calculate_item_priority.register
def _(item: Rucksack) -> int:
    shared_item_type = find_shared_item_type(item)

    return calculate_item_priority(shared_item_type)


@calculate_item_priority.register
def _(item: str) -> int:
    if item.isupper():
        return ord(item) - 38

    return ord(item) - 96


def create_rucksacks_from_packing_lists(path_to_packing_lists: Path) -> tuple[Rucksack]:
    with open(path_to_packing_lists) as packing_lists_file:
        packing_lists = packing_lists_file.read()

    return tuple(
        [pack_into_rucksack(packing_list) for packing_list in packing_lists.split("\n")]
    )


def part_one() -> None:
    rucksacks = create_rucksacks_from_packing_lists("inputs/day03_input.txt")
    sum_of_priorities = sum(map(calculate_item_priority, rucksacks))
    print(sum_of_priorities)


@dataclass(frozen=True)
class Group:
    elf_one: Rucksack
    elf_two: Rucksack
    elf_three: Rucksack


def create_groups_from_rucksacks(path_to_packing_lists: Path) -> tuple[Group]:
    group_size = 3
    rucksacks = create_rucksacks_from_packing_lists(path_to_packing_lists)

    return tuple(
        [
            Group(
                elf_one=rucksacks[group_index],
                elf_two=rucksacks[group_index + 1],
                elf_three=rucksacks[group_index + 2],
            )
            for group_index in range(0, len(rucksacks), group_size)
        ]
    )


def get_group_badge(group: Group) -> str:
    return (
        set(group.elf_one.contents)
        & set(group.elf_two.contents)
        & set(group.elf_three.contents)
    ).pop()


def part_two() -> None:
    groups = create_groups_from_rucksacks("inputs/day03_input.txt")
    badges = map(get_group_badge, groups)
    sum_of_priorities = sum(map(calculate_item_priority, badges))

    print(sum_of_priorities)


if __name__ == "__main__":
    part_one()
    part_two()
