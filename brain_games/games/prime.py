#!/usr/bin/env python3
import random

begin = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def begin_game():
    global random_number
    random_number = random.randint(1, 100)
    question = str(random_number)
    return question


def prime():
    k = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            k += 1
    if (k <= 0):
        result = 'yes'
    else:
        result = 'no'
    return result
