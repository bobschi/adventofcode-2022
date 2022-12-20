Crate = str
Stack = list[Crate]


def peek_top(stack: Stack) -> Crate:
    if stack == []:
        return ""

    return stack[0]
