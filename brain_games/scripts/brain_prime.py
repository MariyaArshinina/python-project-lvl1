#!/usr/bin/env python3
from brain_games.games.prime import begin, prime, begin_game
from brain_games.engine import run_game


def main():
    run_game(begin, prime, begin_game)

    if __name__ == '__main__':
        main()
