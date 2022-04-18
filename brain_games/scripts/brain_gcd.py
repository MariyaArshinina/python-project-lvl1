#!/usr/bin/env python3
from brain_games.games.gcd import gcd, begin
from brain_games.engine import greeting, run_game


def main():
    greeting()
    print(begin)
    run_game(gcd)

    if __name__ == '__main__':
        main()
