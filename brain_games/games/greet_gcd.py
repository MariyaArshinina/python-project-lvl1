#!/usr/bin/env python3
import prompt
import random
import brain_games.games.gcd


def greet_gcd():
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    right_answers = 0
    for x in range(0, 3):
        ran_num1 = random.randint(1, 100)
        ran_num2 = random.randint(1, 100)
        print('Question: ' + str(ran_num1) + '  ' + str(ran_num2))
        num = brain_games.games.gcd.gcd(ran_num1, ran_num2)
        your_answer = prompt.string('Your answer: ')
        if num == int(your_answer):
            print('Correct!')
            right_answers += 1
        else:
            print(your_answer + ' is wrong answer ;(. Correct answer was ' + str(num))
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))
