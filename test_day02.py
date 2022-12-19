import pytest
from solutions.day02 import calculate_score_for_one_round, Sign


@pytest.parametrize(
    "opponent_move,player_move,expected_result",
    [
        (Sign.ROCK, Sign.PAPER, 8),
        (Sign.PAPER, Sign.ROCK, 1),
        (Sign.SCISSORS, Sign.SCISSORS, 6),
    ],
)
def test_calculate_score_for_one_round(
    opponent_move: Sign, player_move: Sign, expected_result: int
):
    result = calculate_score_for_one_round(opponent_move, player_move)
    assert result == expected_result, "Your calculated result is incorrect."

