#!/usr/bin/env python3
from brain_games.games.gcd import begin, get_question_result
from brain_games.engine import run_game


def main():
    run_game(begin, get_question_result)

    if __name__ == '__main__':
        main()
