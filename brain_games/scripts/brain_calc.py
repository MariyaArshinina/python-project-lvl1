#!/usr/bin/env python3
from brain_games.games.calc import begin, calc, begin_game
from brain_games.engine import run_game


def main():
    run_game(begin, calc, begin_game)

    if __name__ == '__main__':
        main()
