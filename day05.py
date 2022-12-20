from pathlib import Path

Crate = str
Stack = list[Crate]
Stackpile = list[Stack]
MovementPlan = list[str]


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


def move_crates(
    from_stack: Stack, to_stack: Stack, number_of_crates: int
) -> tuple[Stack, Stack]:
    new_from_stack, new_to_stack = from_stack, to_stack
    for _ in range(number_of_crates):
        new_from_stack, new_to_stack = move_crate(new_from_stack, new_to_stack)

    return (new_from_stack, new_to_stack)


def read_scenario(
    path_to_scenario: Path,
) -> tuple[Stackpile, MovementPlan]:
    with open(path_to_scenario) as scenario_file:
        scenario = scenario_file.read()

    initial_stack_state, movement_plan = scenario.split("\n\n")
    *stacks, number_of_stacks = initial_stack_state.splitlines()
    stacks.reverse()
    number_of_stacks = len(number_of_stacks.split())

    stackpile = Stackpile([[] for _ in range(number_of_stacks)])
    for level in stacks:
        for stack_id, i in enumerate(range(1, len(stacks[0]), 4)):
            if level[i].strip() != "":
                current_stack = stackpile[stack_id]
                crate = level[i]
                stackpile[stack_id] = put_crate_on_top(current_stack, crate)

    movement_plan = movement_plan.splitlines()

    return (stackpile, movement_plan)


def execute_movement_plan(
    stackpile: Stackpile, movement_plan: MovementPlan
) -> Stackpile:
    ...
