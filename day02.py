from enum import Enum


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
