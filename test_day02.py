import pytest

from day02 import (Result, Sign, calculate_required_move,
                   calculate_score_for_multiple_rounds,
                   calculate_score_for_one_round,
                   read_strategy_guide_from_file)


@pytest.mark.parametrize(
    "opponent_move,player_move,expected_score",
    [
        (Sign.ROCK, Sign.PAPER, 8),
        (Sign.PAPER, Sign.ROCK, 1),
        (Sign.SCISSORS, Sign.SCISSORS, 6),
    ],
)
def test_calculate_score_for_one_round(
    opponent_move: Sign, player_move: Sign, expected_score: int
):
    score = calculate_score_for_one_round(opponent_move, player_move)
    assert score == expected_score, "Your calculated result is incorrect."


def test_calculate_score_for_strategy_guide():
    moves = (
        (Sign.ROCK, Sign.PAPER),
        (Sign.PAPER, Sign.ROCK),
        (Sign.SCISSORS, Sign.SCISSORS),
    )
    expected_result = 15

    result = calculate_score_for_multiple_rounds(moves)
    assert result == expected_result, "Think of a good hint here."


def test_read_strategy_guide_from_file():
    path_to_strategy_guide = "inputs/day02_sample.txt"
    expected_moves = (
        (Sign.ROCK, Sign.ROCK),
        (Sign.PAPER, Sign.ROCK),
        (Sign.SCISSORS, Sign.ROCK),
    )

    moves = read_strategy_guide_from_file(path_to_strategy_guide)

    assert moves == expected_moves


@pytest.mark.parametrize(
    "opponent_move,desired_outcome,expected_move,expected_score",
    [
        (Sign.ROCK, Result.DRAW, Sign.ROCK, 4),
        (Sign.PAPER, Result.LOSS, Sign.ROCK, 1),
        (Sign.SCISSORS, Result.WIN, Sign.ROCK, 7),
        (Sign.SCISSORS, Result.DRAW, Sign.SCISSORS, 6),
        (Sign.SCISSORS, Result.LOSS, Sign.PAPER, 2),
    ],
)
def test_calculate_required_move(
    opponent_move: Sign,
    desired_outcome: Result,
    expected_move: Sign,
    expected_score: int,
):
    move = calculate_required_move(opponent_move, desired_outcome)
    score = calculate_score_for_one_round(opponent_move, move)

    assert move == expected_move, "This is not the correct move."
    assert score == expected_score, "Your score came out wrong."
