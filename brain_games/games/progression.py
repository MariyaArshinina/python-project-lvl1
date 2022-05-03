#!/usr/bin/env/python3
import random

begin = 'What number is missing in the progression?'
min_lot_dig = 5
max_lot_dig = 10
min_com_dif = 2
max_com_dif = 10
min_in_term = 1
max_in_term = 10


def start_progression():
    lot_digits = random.randint(min_lot_dig, max_lot_dig)
    com_dif = random.randint(min_com_dif, max_com_dif)
    initial_term = random.randint(min_in_term, max_in_term)
    stop = initial_term + (lot_digits - 1) * com_dif
    numbers = range(initial_term, stop + com_dif, com_dif)
    return lot_digits, numbers


def get_question_result():
    lot_digits, numbers = start_progression()
    number_list = list(numbers)
    i = random.randint(1, lot_digits - 1)
    member = number_list[i]
    number_list[i] = '..'
    res_number_list = str(number_list).replace("'", " ")
    res_number_list2 = res_number_list.replace(',', ' ')
    res_number_list3 = res_number_list2.replace('[', ' ')
    question = res_number_list3.replace(']', ' ')
    result = str(member)
    return (question, result)
