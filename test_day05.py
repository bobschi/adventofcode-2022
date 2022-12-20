import pytest
from pytest_lazyfixture import lazy_fixture

from day05 import Crate, Stack, get_top, move_crate, peek_top


@pytest.fixture
def stack_a() -> Stack:
    return ["N", "Z"]


@pytest.fixture
def stack_b() -> Stack:
    return ["D", "C", "M"]


@pytest.fixture
def stack_c() -> Stack:
    return ["P"]


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
    "stack_a,stack_b,expected_new_top_a,expected_new_top_b",
    [
        (lazy_fixture("stack_c"), lazy_fixture("stack_a"), "", "P"),
        (lazy_fixture("stack_a"), lazy_fixture("stack_b"), "Z", "N"),
    ],
)
def test_move_crate(
    stack_a: Stack,
    stack_b: Stack,
    expected_new_top_a: Crate,
    expected_new_top_b: Crate,
):
    old_size_a, old_size_b = len(stack_a), len(stack_b)

    new_stack_a, new_stack_b = move_crate(stack_a, stack_b)

    new_top_a, new_top_b = peek_top(new_stack_a), peek_top(new_stack_b)
    new_size_a, new_size_b = len(new_stack_a), len(new_stack_b)

    assert new_size_a - old_size_a + 1 == new_size_b - old_size_b - 1
    assert new_top_a == expected_new_top_a
    assert new_top_b == expected_new_top_b
