#!/usr/bin/env python3
from brain_games.games.progression import progression, begin
from brain_games.engine import greeting, run_game


def main():
    greeting()
    print(begin)
    run_game(progression)

    if __name__ == '__main__':
        main()
