import pytest
from pytest_lazyfixture import lazy_fixture

from day05 import (
    Crate,
    Stack,
    Stackpile,
    read_scenario,
    get_top,
    move_crate,
    move_crates,
    peek_top,
    put_crate_on_top,
)


@pytest.fixture
def stack_a() -> Stack:
    return ["N", "Z"]


@pytest.fixture
def stack_b() -> Stack:
    return ["D", "C", "M"]


@pytest.fixture
def stack_c() -> Stack:
    return ["P"]


@pytest.fixture
def example_stackpile(stack_a, stack_b, stack_c) -> Stackpile:
    return [stack_a, stack_b, stack_c]


@pytest.mark.parametrize(
    "stack,expected_top",
    (
        (lazy_fixture("stack_a"), "N"),
        (lazy_fixture("stack_b"), "D"),
        (lazy_fixture("stack_c"), "P"),
        ([""], ""),
    ),
)
def test_peek_top(stack: Stack, expected_top: Crate):
    top = peek_top(stack)

    assert top == expected_top


@pytest.mark.parametrize(
    "stack,expected_new_stack,expected_old_top,expected_new_top",
    (
        (lazy_fixture("stack_a"), ["Z"], "N", "Z"),
        (lazy_fixture("stack_b"), ["C", "M"], "D", "C"),
        (lazy_fixture("stack_c"), [], "P", ""),
    ),
)
def test_get_top(
    stack: Stack,
    expected_new_stack: Stack,
    expected_old_top: Crate,
    expected_new_top: Crate,
):
    old_stack_size = len(stack)
    old_top, new_stack = get_top(stack)
    new_top = peek_top(new_stack)
    new_stack_size = len(new_stack)

    assert new_stack_size == old_stack_size - 1, "You did not take the top off."
    assert old_top == expected_old_top, "You took off the wrong thing."
    assert new_stack == expected_new_stack, "Our new stack looks weird."
    assert new_top == expected_new_top, "You've got the wrong top on there, mate."


@pytest.mark.parametrize(
    "stack,crate,expected_stack",
    [
        (["A", "B", "C"], "D", ["D", "A", "B", "C"]),
        (["N", "Z"], "X", ["X", "N", "Z"]),
        (["D", "C", "M"], "R", ["R", "D", "C", "M"]),
    ],
)
def test_put_crate_on_top(stack: Stack, crate: Crate, expected_stack: Stack):
    new_stack = put_crate_on_top(stack, crate)

    assert new_stack == expected_stack


@pytest.mark.parametrize(
    "from_stack,to_stack,expected_new_top_a,expected_new_top_b",
    [
        (lazy_fixture("stack_c"), lazy_fixture("stack_a"), "", "P"),
        (lazy_fixture("stack_b"), ["T"], "C", "D"),
    ],
)
def test_move_crate(
    from_stack: Stack,
    to_stack: Stack,
    expected_new_top_a: Crate,
    expected_new_top_b: Crate,
):
    old_size_a, old_size_b = len(from_stack), len(to_stack)

    new_stack_a, new_stack_b = move_crate(from_stack, to_stack)

    new_top_a, new_top_b = peek_top(new_stack_a), peek_top(new_stack_b)
    new_size_a, new_size_b = len(new_stack_a), len(new_stack_b)

    assert new_size_a - old_size_a + 1 == new_size_b - old_size_b - 1
    assert new_top_a == expected_new_top_a
    assert new_top_b == expected_new_top_b


@pytest.mark.parametrize(
    "from_stack,to_stack,number_of_crates,expected_new_from_stack,expected_new_to_stack",
    [
        (["A", "B", "C"], [], 3, [], ["C", "B", "A"]),
        (["A", "B"], ["C", "D"], 1, ["B"], ["A", "C", "D"]),
    ],
)
def test_move_multiple_crates(
    from_stack: Stack,
    to_stack: Stack,
    number_of_crates: int,
    expected_new_from_stack: Stack,
    expected_new_to_stack: Stack,
):
    new_from_stack, new_to_stack = move_crates(from_stack, to_stack, number_of_crates)

    assert new_from_stack == expected_new_from_stack
    assert new_to_stack == expected_new_to_stack


def test_read_scenario():
    stackpile, movement_plan = read_scenario("inputs/day05_sample.txt")

    assert len(stackpile) == 3
    assert len(movement_plan) == 4
