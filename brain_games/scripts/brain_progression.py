#!/usr/bin/env python3
from brain_games.games.progression import progression, begin_game
from brain_games.engine import run_game


def main():
    run_game(progression, begin_game)

    if __name__ == '__main__':
        main()
