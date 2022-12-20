from dataclasses import dataclass


@dataclass(frozen=True)
class Rucksack:
    compartment_one: str
    compartment_two: str


def pack_into_rucksack(contents: str) -> Rucksack:
    length = len(contents)
    return Rucksack(
        compartment_one=contents[: length // 2],
        compartment_two=contents[length // 2 :],
    )
