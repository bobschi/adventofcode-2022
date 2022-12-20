Crate = str
Stack = list[Crate]


def peek_top(stack: Stack) -> Crate:
    if stack == []:
        return ""

    return stack[0]


def get_top(stack: Stack) -> tuple[Crate, Stack]:
    old_top = stack[0]
    new_stack = stack[1:]
    return (old_top, new_stack)


def put_crate_on_top(stack: Stack, crate: Crate) -> Stack:
    new_stack = [crate] + stack
    return new_stack


def move_crate(from_stack: Stack, to_stack: Stack) -> tuple[Stack, Stack]:
    crate_to_move, new_from_stack = get_top(from_stack)
    new_to_stack = put_crate_on_top(to_stack, crate_to_move)

    return (new_from_stack, new_to_stack)
