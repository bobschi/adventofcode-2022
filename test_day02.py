import pytest
from day02 import calculate_score_for_one_round, Sign


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
