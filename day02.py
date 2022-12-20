from enum import Enum
from pathlib import Path

import typer


class Sign(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


OUTCOMES: dict[Sign, dict[Sign, Result]] = {
    Sign.ROCK: {
        Sign.ROCK: Result.DRAW,
        Sign.PAPER: Result.WIN,
        Sign.SCISSORS: Result.LOSS,
    },
    Sign.PAPER: {
        Sign.ROCK: Result.LOSS,
        Sign.PAPER: Result.DRAW,
        Sign.SCISSORS: Result.WIN,
    },
    Sign.SCISSORS: {
        Sign.ROCK: Result.WIN,
        Sign.PAPER: Result.LOSS,
        Sign.SCISSORS: Result.DRAW,
    },
}


def calculate_score_for_one_round(opponent_move: Sign, player_move: Sign) -> int:
    return player_move.value + OUTCOMES[opponent_move][player_move].value


Move = tuple[Sign, Sign]
Moves = tuple[Move]


def calculate_score_for_multiple_rounds(moves: Moves) -> int:
    return sum([calculate_score_for_one_round(move[0], move[1]) for move in moves])


def read_strategy_guide_from_file(path_to_strategy_guide: Path) -> Moves:
    opponent_moves = {"A": Sign.ROCK, "B": Sign.PAPER, "C": Sign.SCISSORS}
    player_moves = {"X": Sign.ROCK, "Y": Sign.PAPER, "Z": Sign.SCISSORS}

    with open(path_to_strategy_guide, "r") as strategy_guide_file:
        strategy_guide = strategy_guide_file.read()

    moves: list[Move] = []
    for line in strategy_guide.split("\n"):
        opponent_move, player_move = line.split(" ")
        moves.append((opponent_moves[opponent_move], player_moves[player_move]))

    return tuple(moves)


def calculate_required_move(opponent_move: Sign, desired_outcome: Result) -> Sign:
    for move, result in OUTCOMES[opponent_move].items():
        if result == desired_outcome:
            return move


def solve_day_two(
    path_to_strategy_guide: Path = typer.Argument("inputs/day02_input.txt"),
) -> None:
    moves = read_strategy_guide_from_file(path_to_strategy_guide)
    score = calculate_score_for_multiple_rounds(moves)

    print(f"The final score is {score}")


if __name__ == "__main__":
    typer.run(solve_day_two)
