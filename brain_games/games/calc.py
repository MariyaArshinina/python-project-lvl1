#!/usr/bin/env python3
import random

begin = 'What is the result of expressions?'


def begin_game():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operand = ['+', '-', '*']
    random_operand = random.choice(operand)
    global question
    question = str(random_number1) + ' ' + str(
        random_operand) + ' ' + str(random_number2)
    return question


def calc():
    result = eval(question)
    result = str(result)
    return result
