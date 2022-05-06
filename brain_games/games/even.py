#!/usr/bin/env python3
import random

begin = 'Answer "yes" if the number is even, otherwise answer "no".'
beg_range = 1
end_range = 100


def begin_game():
    random_number = random.randint(beg_range, end_range)
    return random_number


def is_even(random_number):
    return random_number % 2 == 0


def get_question_result():
    random_number = begin_game()
    question = str(random_number)
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return (question, result)
