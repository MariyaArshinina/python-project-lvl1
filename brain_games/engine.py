#!/usr/bin/env python3
import prompt

number_rounds = 3


def run_game(begin, get_question_result):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(begin)
    right_answers = 0
    for x in range(number_rounds):
        question, result = get_question_result()
        print('Question:' + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            right_answers += 1
        else:
            print(
                '"' + answer + '" is wrong answer ;(. '
                'Correct answer was "' + result + '"')
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))
