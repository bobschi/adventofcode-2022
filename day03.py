from dataclasses import dataclass
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


def calculate_shared_item_priority(rucksack: Rucksack) -> int:
    shared_item_type = find_shared_item_type(rucksack)
    if shared_item_type.isupper():
        return ord(shared_item_type) - 38

    return ord(shared_item_type) - 96


def create_rucksacks_from_packing_lists(path_to_packing_lists: Path) -> tuple[Rucksack]:
    with open(path_to_packing_lists) as packing_lists_file:
        packing_lists = packing_lists_file.read()

    return tuple(
        [pack_into_rucksack(packing_list) for packing_list in packing_lists.split("\n")]
    )
