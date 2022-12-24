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


def number_of_visible_trees_in_row(row: int, direction: Direction, map: Map) -> int:
    row_looked_at = map[row]

    if direction == Direction.RIGHT:
        row_looked_at.reverse()

    return visible_trees_in_line_of_tress(row_looked_at)


def number_of_visible_trees_in_column(
    column: int, direction: Direction, map: Map
) -> int:
    column_looked_at = [row[column] for row in map]

    if direction == Direction.UP:
        column_looked_at.reverse()

    return visible_trees_in_line_of_tress(column_looked_at)


def visible_trees_in_line_of_tress(line_of_trees: list[int]) -> int:
    def are_neighbors_smaller(position: int) -> bool:
        height_at_position = line_of_trees[position]

        for tree in line_of_trees[:position]:
            if tree >= height_at_position:
                return False

        return True

    count = 0
    for position, height in enumerate(line_of_trees):
        if height == 0:
            continue

        if not are_neighbors_smaller(position):
            continue

        count = count + 1

    return count
