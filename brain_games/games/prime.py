#!/usr/bin/env python3
import random

begin = 'Answer "yes" if given number is prime. Otherwise answer "no".'
beg_range = 1
end_range = 100


def begin_game():
    random_number = random.randint(beg_range, end_range)
    return random_number


def prime(random_number):
    k = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            k += 1
    return k <= 0


def get_question_result():
    random_number = begin_game()
    question = str(random_number)
    if prime(random_number):
        result = 'yes'
    else:
        result = 'no'
    return (question, result)
