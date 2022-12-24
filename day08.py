import enum


class Direction(enum.Enum):
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()


Map = list[list[int]]


def visible_trees_in_line(map: Map, direction: Direction, line: int) -> int:
    if direction in [Direction.UP, Direction.DOWN]:
        line_of_trees = [row[line] for row in map]

    if direction in [Direction.LEFT, Direction.RIGHT]:
        line_of_trees = map[line]

    if direction in [Direction.UP, Direction.RIGHT]:
        line_of_trees.reverse()

    def are_neighbors_smaller(trees: list[int], current_position: int) -> bool:
        for tree in trees[:current_position]:
            if tree >= trees[current_position]:
                return False

        return True

    count = 0
    for spot, height in enumerate(line_of_trees):
        if height == 0 or not are_neighbors_smaller(line_of_trees, spot):
            continue

        count = count + 1

    return count
