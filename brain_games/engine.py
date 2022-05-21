#!/usr/bin/env python3
import prompt

ROUNDS_COUNT = 3


def run_game(BEGIN, get_question_correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(BEGIN)
    right_answers = 0
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_correct_answer()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            right_answers += 1
        else:
            print(
                '"' + answer + '" is wrong answer ;(. '
                'Correct answer was "' + correct_answer + '"')
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))
