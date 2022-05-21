#!/usr/bin/env python3
import random

BEGIN = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def gcd(random_number1, random_number2):
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
        result = random_number1 + random_number2
    return result


def get_question_correct_answer():
    random_number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    random_number2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    question = str(random_number1) + ' ' + str(random_number2)
    result = gcd(random_number1, random_number2)
    correct_answer = str(result)
    return question, correct_answer
