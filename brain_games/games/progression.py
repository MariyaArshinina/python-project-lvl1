#!/usr/bin/env/python3
import random

BEGIN = 'What number is missing in the progression?'
MIN_LOT_DIG = 5
MAX_LOT_DIG = 10
MIN_COM_DIF = 2
MAX_COM_DIF = 10
MIN_IN_TERM = 1
MAX_IN_TERM = 10


def calculation_progression_parameters():
    length = random.randint(MIN_LOT_DIG, MAX_LOT_DIG)
    com_dif = random.randint(MIN_COM_DIF, MAX_COM_DIF)
    initial_term = random.randint(MIN_IN_TERM, MAX_IN_TERM)
    return length, com_dif, initial_term


def generate_progression(length, com_dif, initial_term):
    stop = initial_term + (length - 1) * com_dif
    numbers = range(initial_term, stop + com_dif, com_dif)
    return numbers


def get_progression_list(numbers):
    number_list = list(numbers)
    i = random.randint(1, len(number_list) - 1)
    member = number_list[i]
    number_list[i] = '..'
    return member, number_list


def get_question_correct_answer():
    length, com_dif, initial_term = calculation_progression_parameters()
    numbers = generate_progression(length, com_dif, initial_term)
    member, number_list = get_progression_list(numbers)
    question = " ".join(str(x) for x in number_list)
    correct_answer = str(member)
    return question, correct_answer
