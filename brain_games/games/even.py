#!/usr/bin/env python3
import random
begin = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    random_number = random.randint(1, 100)
    question = str(random_number)
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result


question, result = even()
