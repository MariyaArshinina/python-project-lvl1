#!/usr/bin/env python3
import random
begin = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    random_number = random.randint(1, 100)
    k = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            k += 1
    if (k <= 0):
        result = 'yes'
    else:
        result = 'no'
    question = str(random_number)
    return question, result


question, result = prime()
