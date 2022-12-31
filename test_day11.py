import pytest

from day11 import Monkey, do_inspection_round, spawn_monkey


@pytest.fixture
def sample_monkey_block() -> str:
    return (
        "Monkey 0:\n"
        "Starting items: 79, 98\n"
        "Operation: new = old * 19\n"
        "Test: divisible by 23\n"
        "If true: throw to monkey 2\n"
        "If false: throw to monkey 3"
    )


@pytest.fixture
def monkey_0() -> Monkey:
    return Monkey(0, [79, 98], "old * 19", 23, 2, 3)


@pytest.fixture
def monkey_1() -> Monkey:
    return Monkey(1, [54, 65, 75, 74], "old + 6", 19, 2, 0)


def test_spawn_monkey(sample_monkey_block: str, monkey_0: Monkey) -> None:
    spawned_monkey = spawn_monkey(sample_monkey_block)

    assert spawned_monkey == monkey_0


def test_throwing_item(monkey_0: Monkey, monkey_1: Monkey) -> None:
    monkey_0.throw_item(monkey_1)

    assert monkey_0.worry_levels == [98]
    assert monkey_1.worry_levels == [54, 65, 75, 74, 79]


def test_inspect_item(monkey_0: Monkey, monkey_1: Monkey) -> None:
    assert monkey_0.inspect_item() == 3
    monkey_0.throw_item(monkey_1)
    assert monkey_0.inspect_item() == 3
    assert monkey_1.inspect_item() == 0


def test_inspect_item_changes_worry_level(monkey_0: Monkey) -> None:
    monkey_0.inspect_item()

    assert monkey_0.worry_levels[0] == 500


def test_inspect_item_and_throw_passes_on_correct_worry_level(
    monkey_0: Monkey, monkey_1: Monkey
) -> None:
    monkey_0.inspect_item()
    monkey_0.throw_item(monkey_1)

    assert monkey_1.worry_levels[-1] == 500


def test_inspect_items_raises_inspection_count(monkey_0: Monkey) -> None:
    assert monkey_0.inspection_count == 0
    monkey_0.inspect_item()
    assert monkey_0.inspection_count == 1
    monkey_0.inspect_item()
    assert monkey_0.inspection_count == 2


def test_inspection_round(monkey_0: Monkey, monkey_1: Monkey) -> None:
    monkey_0.success_monkey_id = 1
    monkey_0.failure_monkey_id = 1
    monkey_1.success_monkey_id = 0
    monkey_1.failure_monkey_id = 0

    monkeys = [monkey_0, monkey_1]

    do_inspection_round(monkeys)

    assert len(monkeys[0].worry_levels) == 6
    assert len(monkeys[1].worry_levels) == 0
