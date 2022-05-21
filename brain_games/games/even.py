#!/usr/bin/env python3
import random

BEGIN = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def is_even(random_number):
    return random_number % 2 == 0


def get_question_correct_answer():
    random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    question = "{}".format(random_number)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
