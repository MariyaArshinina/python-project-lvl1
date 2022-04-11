#!/usr/bin/env python3
import random
begin = 'What is the result of expressions?'


def calc():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operand = ['+', '-', '*']
    random_operand = random.choice(operand)
    question = str(random_number1) + random_operand + str(random_number2)
    result = eval(question)
    return question, result

question, result = calc()
