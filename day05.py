Crate = str
Stack = list[Crate]


def peek_top(stack: Stack) -> Crate:
    if stack == []:
        return ""

    return stack[0]


def get_top(stack: Stack) -> tuple[Crate, Stack]:
    old_top = stack.pop(0)
    return (old_top, stack)


def move_crate(from_stack: Stack, to_stack: Stack, number: int) -> tuple[Stack, Stack]:
    ...
