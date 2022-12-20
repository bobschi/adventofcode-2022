import pytest
from pytest_lazyfixture import lazy_fixture

from day05 import Crate, Stack, peek_top


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
