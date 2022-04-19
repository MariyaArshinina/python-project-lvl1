#!/usr/bin/env/python3
import random


def begin_game():
    begin = 'What number is missing in the progression?'
    return begin


begin = begin_game()


def progression():
    lot_digits = random.randint(5, 10)
    step = random.randint(2, 10)
    start = random.randint(1, 10)
    stop = start + (lot_digits - 1) * step
    numbers = range(start, stop + step, step)
    number_list = list(numbers)
    i = random.randint(1, lot_digits - 1)
    result = number_list[i]
    number_list[i] = '..'
    res_number_list = str(number_list).replace("'", " ")
    res_number_list2 = res_number_list.replace(',', ' ')
    res_number_list3 = res_number_list2.replace('[', ' ')
    question = res_number_list3.replace(']', ' ')
    result = str(result)
    return question, result


question, result = progression()
