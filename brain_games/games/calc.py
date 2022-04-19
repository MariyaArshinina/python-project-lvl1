#!/usr/bin/env python3
import random


def begin_game():
    begin = 'What is the result of expressions?'
    return begin


begin = begin_game()


def calc():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operand = ['+', '-', '*']
    random_operand = random.choice(operand)
    question = str(random_number1) + random_operand + str(random_number2)
    result = eval(question)
    result = str(result)
    return question, result


question, result = calc()
