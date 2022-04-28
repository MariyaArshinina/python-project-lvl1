#!/usr/bin/env python3
import random

begin = 'Find the greatest common divisor of given numbers.'


def begin_game():
    global random_number1
    random_number1 = random.randint(1, 100)
    global random_number2
    random_number2 = random.randint(1, 100)
    question = str(random_number1) + ' ' + str(random_number2)
    return question


def gcd():
    if random_number1 > random_number2:
        temp = random_number2
    else:
        temp = random_number1
    for i in range(1, temp + 1):
        if ((random_number1 % i == 0) and (random_number2 % i == 0)):
            result = i
            result = str(result)
    return result
