#!/usr/bin/env python3
from brain_games.games.even import even, begin
from brain_games.engine import greeting, run_game


def main():
    greeting()
    print(begin)
    run_game(even)

    if __name__ == '__main__':
        main()
