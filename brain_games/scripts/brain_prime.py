#!/usr/bin/env python3
from brain_games.games.prime import BEGIN, get_question_correct_answer
from brain_games.engine import run_game


def main():
    run_game(BEGIN, get_question_correct_answer)

    if __name__ == '__main__':
        main()
