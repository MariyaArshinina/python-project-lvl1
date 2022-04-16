#!/usr/bin/env python3
import prompt


def greeting():
    print('Welcom to the Brain Games!')
    global name
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))


def run_game(game):
    right_answers = 0
    for x in range(0, 3):
        question, result = game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            right_answers += 1
        else:
            print(
                answer + ' is wrong answer ;(. '
                'Correct answer was ' + result)
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))
