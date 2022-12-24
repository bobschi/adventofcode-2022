import enum


class Direction(enum.IntEnum):
    UP = 1
    RIGHT = 1
    DOWN = 0
    LEFT = 0


Map = list[list[int]]


def number_of_trees_visible_from_direction(
    position: int, direction: Direction, map: Map
) -> int:
    ...

def is_tree(tree_height: int) -> bool:
    return tree_height >= 1


def number_of_visible_trees_in_row(row: int, direction: Direction, map: Map) -> int:
    row_looked_at = map[row]

    if direction == Direction.RIGHT:
        row_looked_at.reverse()


    def are_neighbors_smaller(position: int) -> bool:
        height_at_position = row_looked_at[position]

        for tree in row_looked_at[:position]:
            if tree >= height_at_position:
                return False

        return True

    count: int = 0
    for position, tree in enumerate(row_looked_at):
        if not is_tree(tree):
            continue

        if not are_neighbors_smaller(position):
            continue

        count = count + 1

    return count


def number_of_visible_trees_in_column(
    column: int, direction: Direction, map: Map
) -> int:
    ...
