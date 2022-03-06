#!/usr/bin/env python3
import prompt
import random
import brain_games.games.greet


def brain_calc():
    right_answers = 0
    for x in range(0, 3):
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        operand = ['+', '-', '*']
        random_operand = random.choice(operand)
        expression = str(random_number1) + random_operand + str(random_number2)
        print('Question: ' + expression)
        your_answer = prompt.string('Your answer: ')
        if eval(expression) == int(your_answer):
            print('Correct!')
            right_answers += 1
        else:
            print(your_answer + ' is wrong answer ;(. Correct answer was ' + str(eval(expression)))
            print('Let\'s try again, {}!'.format(brain_games.games.greet.name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(brain_games.games.greet.name))
