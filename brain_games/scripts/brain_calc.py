#!/usr/bin/env python3
from brain_games.games.calc import brain_calc
import brain_games.games.greet


def main():
    print('Welcome to the Brain Games!')
    brain_games.games.greet.greet()
    brain_calc()

    if __name__ == '__main__':
        main()
