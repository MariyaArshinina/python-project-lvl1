#!/usr/bin/env python3
import random

begin = 'Find the greatest common divisor of given numbers.'
beg_range = 1
end_range = 100


def begin_game():
    random_number1 = random.randint(beg_range, end_range)
    random_number2 = random.randint(beg_range, end_range)
    return random_number1, random_number2


def gcd(random_number1, random_number2):
    if random_number1 > random_number2:
        temp = random_number2
    else:
        temp = random_number1
    for i in range(1, temp + 1):
        if ((random_number1 % i == 0) and (random_number2 % i == 0)):
            result = i
    return result


def get_question_result():
    random_number1, random_number2 = begin_game()
    question = str(random_number1) + ' ' + str(random_number2)
    result = gcd(random_number1, random_number2)
    result = str(result)
    return (question, result)
