#!/usr/bin/env/python3
import prompt
import random


def progression():
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    right_answers = 0
    for x in range(0, 3):
        lot_digits = random.randint(5, 10)
        step = random.randint(2, 10)
        start = random.randint(1, 10)
        stop = start + (lot_digits - 1) * step
        numbers = range(start, stop + step, step)
        number_list = list(numbers)
        i = random.randint(1, lot_digits - 1)
        answer = number_list[i]
        number_list[i] = '..'
        res_number_list = str(number_list).replace("'", " ")
        res_number_list2 = res_number_list.replace(',', ' ')
        res_number_list3 = res_number_list2.replace('[', ' ')
        res_number_list4 = res_number_list3.replace(']', ' ')
        print('Question: ' + res_number_list4)
        your_answer = prompt.string('Your answer: ')
        if int(answer) == int(your_answer):
            print('Correct!')
            right_answers += 1
        else:
            print(
                your_answer + ' is wrong answer ;(.'
                'Correct answer was ' + str(answer))
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))
