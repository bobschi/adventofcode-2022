from dataclasses import dataclass
from typing import Self

SESSION = open(".aoc-token").read()


@dataclass
class Monkey:
    id: int
    worry_levels: list[int]
    # TODO: Figure out how to make this into a Callable, ideally
    operation: str
    divisor: int
    success_monkey_id: int
    failure_monkey_id: int

    def test(self, worry_level: int) -> bool:
        return worry_level % self.divisor == 0

    def throw_item(self, other: Self) -> None:
        item_to_throw = self.worry_levels.pop(0)
        other.worry_levels.append(item_to_throw)


def read_scenario(scenario: str) -> list[Monkey]:
    return [spawn_monkey(monkey_block) for monkey_block in scenario.split("\n\n")]


def spawn_monkey(monkey_block: str) -> Monkey:
    new_monkey_values = {}
    for line in monkey_block.splitlines():
        line = line.replace(":", "")
        line = line.replace(",", "")

        match line.split():
            case ["Monkey", id]:
                new_monkey_values["id"] = int(id)

            case ["Starting", "items", *items]:
                new_monkey_values["worry_levels"] = list(map(int, items))

            case ["Operation", *operation]:
                new_monkey_values["operation"] = " ".join(operation)

            case ["Test", "divisible", "by", divisor]:
                new_monkey_values["divisor"] = int(divisor)

            case ["If", "true", *_, success_monkey_id]:
                new_monkey_values["success_monkey_id"] = int(success_monkey_id)

            case ["If", "false", *_, failure_monkey_id]:
                new_monkey_values["failure_monkey_id"] = int(failure_monkey_id)

    return Monkey(**new_monkey_values)
