from dataclasses import dataclass


@dataclass(frozen=True)
class Rucksack:
    compartment_one: str
    compartment_two: str

    @property
    def shared_item_type(self) -> str:
        return (set(self.compartment_one) & set(self.compartment_two)).pop()


def pack_into_rucksack(contents: str) -> Rucksack:
    length = len(contents)
    return Rucksack(
        compartment_one=contents[: length // 2],
        compartment_two=contents[length // 2 :],
    )
