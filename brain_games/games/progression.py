#!/usr/bin/env/python3
import random

begin = 'What number is missing in the progression?'


def start_progression():
    global lot_digits
    lot_digits = random.randint(5, 10)
    com_dif = random.randint(2, 10)
    initial_term = random.randint(1, 10)
    stop = initial_term + (lot_digits - 1) * com_dif
    numbers = range(initial_term, stop + com_dif, com_dif)
    return numbers


def begin_game():
    number_list = list(start_progression())
    i = random.randint(1, lot_digits - 1)
    global member
    member = number_list[i]
    number_list[i] = '..'
    res_number_list = str(number_list).replace("'", " ")
    res_number_list2 = res_number_list.replace(',', ' ')
    res_number_list3 = res_number_list2.replace('[', ' ')
    question = res_number_list3.replace(']', ' ')
    return question


def progression():
    result = member
    result = str(result)
    return result
