from dataclasses import dataclass


@dataclass(frozen=True)
class Rucksack:
    compartment_one: str
    compartment_two: str


def pack_into_rucksack(contents) -> Rucksack:
    ...
