#!/usr/bin/env python3
from brain_games.games.even import even, begin_game
from brain_games.engine import run_game


def main():
    run_game(even, begin_game)

    if __name__ == '__main__':
        main()
