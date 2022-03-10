#!/usr/bin/env python3
from brain_games.games.even import brain_even
import brain_games.games.greet_even


def main():
    print('Welcome to the Brain Games!')
    brain_games.games.greet_even.greet_even()
    brain_even()

    if __name__ == '__main__':
        main()
