#!/usr/bin/env python3
import random

begin = 'What is the result of expressions?'
beg_range = 1
end_range = 100


def get_question_result():
    random_number1 = random.randint(beg_range, end_range)
    random_number2 = random.randint(beg_range, end_range)
    operand = ['+', '-', '*']
    random_operand = random.choice(operand)
    question = ' ' + str(random_number1) + ' ' + str(
        random_operand) + ' ' + str(random_number2)
    result = eval(question)
    result = str(result)
    return (question, result)
