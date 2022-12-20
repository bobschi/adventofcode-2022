import pytest
from pytest_lazyfixture import lazy_fixture

from day05 import Crate, Stack, get_top, peek_top


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
