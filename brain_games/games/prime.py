#!/usr/bin/env python3
import random

BEGIN = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def is_prime(random_number):
    k = 0
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            k = 1
            return
    return k <= 0


def get_question_correct_answer():
    random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    question = str(random_number)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
