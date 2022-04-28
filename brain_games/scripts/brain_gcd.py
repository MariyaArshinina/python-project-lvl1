#!/usr/bin/env python3
from brain_games.games.gcd import begin, gcd, begin_game
from brain_games.engine import run_game


def main():
    run_game(begin, gcd, begin_game)

    if __name__ == '__main__':
        main()
