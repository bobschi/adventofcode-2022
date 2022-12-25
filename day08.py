from functools import reduce
from itertools import chain
from operator import mul
from pathlib import Path

Map = list[list[int]]


def number_of_lines(map: Map) -> int:
    return len(map)


def number_of_columns(map: Map) -> int:
    return len(map[0])


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

    return sum(chain(*visible_trees))


def max_scenic_score(height_map: Map) -> Map:
    def trees_visible(height: int, line_of_trees: list[int]) -> int:
        count = 0
        for tree in line_of_trees:
            count += 1
            if tree >= height:
                break
        return count

    lines = number_of_lines(height_map)
    scenic_scores = [[0] * number_of_columns(height_map) for _ in range(lines)]

    for line_index, line in enumerate(height_map):
        for column_index, height in enumerate(line):
            viewing_distances = []

            looking_up = [height_map[i][column_index] for i in range(line_index)]
            viewing_distances.append(trees_visible(height, reversed(looking_up)))

            looking_left = line[:column_index]
            viewing_distances.append(trees_visible(height, reversed(looking_left)))

            looking_down = [
                height_map[i][column_index] for i in range(line_index + 1, lines)
            ]
            viewing_distances.append(trees_visible(height, looking_down))

            looking_right = line[column_index + 1 :]
            viewing_distances.append(trees_visible(height, looking_right))

            scenic_scores[line_index][column_index] = reduce(mul, viewing_distances)

    return max(chain(*scenic_scores))


def read_map(path_to_map: Path) -> Map:
    with open(path_to_map, "r") as map_file:
        map_contents = map_file.readlines()

    return [[int(height) for height in list(line.strip())] for line in map_contents]


def solve_part_one(map: Map) -> None:
    print(f"The solution to part one is {number_of_visible_trees_from_outside(map)}")


def solve_part_two(map: Map) -> None:
    print(f"The solution to part two is {max_scenic_score(map)}")


if __name__ == "__main__":
    map = read_map("inputs/day08_input.txt")
    solve_part_one(map)
    solve_part_two(map)
