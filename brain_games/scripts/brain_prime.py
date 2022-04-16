#!/usr/bin/env python3
from brain_games.games.prime import prime, begin
from brain_games.engine import greeting, run_game


def main():
    greeting()
    print(begin)
    prime()
    run_game(prime)

    if __name__ == '__main__':
        main()
