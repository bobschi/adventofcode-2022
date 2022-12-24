from itertools import chain
from pathlib import Path

Map = list[list[int]]


def number_of_lines(map: Map) -> int:
    return len(map)


def number_of_columns(map: Map) -> int:
    return len(map[0])


# 30373
# 25512
# 65332
# 33549
# 35390
def visible_trees_from_outside(map: Map) -> Map:
    columns = number_of_columns(map)
    lines = number_of_lines(map)
    visible_trees = [[0] * columns for _ in range(lines)]

    for line_index, line in enumerate(map):
        for column_index, height in enumerate(line):
            tests = [
                line_index in [0, columns - 1],
                column_index in [0, lines - 1],
                all([tree < height for tree in line[:column_index]]),
                all([tree < height for tree in line[column_index + 1 :]]),
                all([map[i][column_index] < height for i in range(line_index)]),
                all(
                    [
                        map[i][column_index] < height
                        for i in range(line_index + 1, lines)
                    ]
                ),
            ]

            if any(tests):
                visible_trees[line_index][column_index] = 1

    return visible_trees


def number_of_visible_trees_from_outside(map: Map) -> int:
    visible_trees = visible_trees_from_outside(map)
    from pprint import pprint

    pprint(map)
    pprint(visible_trees)
    return sum(chain(*visible_trees))


def read_map(path_to_map: Path) -> Map:
    with open(path_to_map, "r") as map_file:
        map_contents = map_file.readlines()

    return [[int(height) for height in list(line.strip())] for line in map_contents]


def solve_part_one() -> None:
    map = read_map("inputs/day08_input.py")
    visible_trees = visible_trees_from_outside(map)

    print(f"The solution to part one is {visible_trees}")
