#!/usr/bin/env python3
import random

BEGIN = 'What is the result of expressions?'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_question_correct_answer():
    random_number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    random_number2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    operand = ['+', '-', '*']
    random_operand = random.choice(operand)
    question = "{} {} {}".format(
        random_number1, random_operand, random_number2)
    result = eval(question)
    correct_answer = str(result)
    return question, correct_answer
