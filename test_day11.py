import pytest

from day11 import Monkey, spawn_monkey


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


def test_spawn_monkey(sample_monkey_block: str) -> None:
    expected_monkey = Monkey(0, [79, 98], "new = old * 19", 23, 2, 3)

    spawned_monkey = spawn_monkey(sample_monkey_block)

    assert expected_monkey == spawned_monkey
