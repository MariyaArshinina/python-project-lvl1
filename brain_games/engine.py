#!/usr/bin/env python3
import prompt


def run_game(begin, game, begin_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(begin)
    right_answers = 0
    for x in range(0, 3):
        question = begin_game()
        result = game()
        print('Question: ' + question)
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
