#!/usr/bin/env python3
import random

begin = 'Answer "yes" if the number is even, otherwise answer "no".'


def begin_game():
    global random_number
    random_number = random.randint(1, 100)
    question = str(random_number)
    return question


def even():
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
