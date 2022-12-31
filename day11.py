from dataclasses import dataclass
from operator import mul
from typing import Self

import aocd

SESSION = open(".aoc-token").read()


@dataclass
class Monkey:
    id: int
    worry_levels: list[int]
    operation: str
    divisor: int
    success_monkey_id: int
    failure_monkey_id: int
    inspection_count: int = 0

    def test(self, worry_level: int) -> bool:
        return worry_level % self.divisor == 0

    def throw_item(self, other: Self) -> None:
        item_to_throw = self.worry_levels.pop(0)
        other.worry_levels.append(item_to_throw)

    def inspect_item(self) -> int:
        new_worry_level = eval(self.operation.replace("old", str(self.worry_levels[0])))
        new_worry_level //= 3
        self.worry_levels[0] = new_worry_level

        self.inspection_count += 1

        if self.test(self.worry_levels[0]):
            return self.success_monkey_id

        else:
            return self.failure_monkey_id


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

            case ["Operation", "new", "=", *operation]:
                new_monkey_values["operation"] = " ".join(operation)

            case ["Test", "divisible", "by", divisor]:
                new_monkey_values["divisor"] = int(divisor)

            case ["If", "true", *_, success_monkey_id]:
                new_monkey_values["success_monkey_id"] = int(success_monkey_id)

            case ["If", "false", *_, failure_monkey_id]:
                new_monkey_values["failure_monkey_id"] = int(failure_monkey_id)

    return Monkey(**new_monkey_values)


def do_inspection_round(monkeys: list[Monkey]) -> None:
    for monkey in monkeys:
        while monkey.worry_levels:
            throw_to = monkey.inspect_item()
            monkey.throw_item(monkeys[throw_to])


def get_level_of_monkey_business(monkeys: list[Monkey]) -> int:
    monkeys_by_inpsection_count = list(
        sorted(monkeys, key=lambda monkey: monkey.inspection_count, reverse=True)
    )

    return (
        monkeys_by_inpsection_count[0].inspection_count
        * monkeys_by_inpsection_count[1].inspection_count
    )


def solve_part_one() -> None:
    data = aocd.get_data(session=SESSION, day=11, year=2022)

    monkeys = read_scenario(data)
    for _ in range(20):
        do_inspection_round(monkeys)

    solution = get_level_of_monkey_business(monkeys)

    aocd.submit(answer=solution, part="a", day=11, year=2022, session=SESSION)


if __name__ == "__main__":
    solve_part_one()
