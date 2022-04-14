#!/usr/bin/env python3
from brain_games.games.calc import calc, begin
from brain_games.engine import greeting, run_game


def main():
    greeting()
    print(begin)
    calc()
    run_game(calc)

    if __name__ == '__main__':
        main()
