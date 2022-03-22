#!/usr/bin/env python3
import prompt
import random


def greet_prime():
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answers = 0
    for x in range(0, 3):
        ran_number = random.randint(1, 100)
        print('Question: ' + str(ran_number))
        k = 0
        for i in range(2, ran_number // 2 + 1):
            if (ran_number % i == 0):
                k += 1
        if (k <= 0):
            prime_number = 1
        else:
            prime_number = 0
        your_answer = prompt.string('Your answer: ')
        if (prime_number == 1 and your_answer == 'yes') or (prime_number == 0 and your_answer == 'no'):
            print('Correct!')
            right_answers += 1
        else:
            print('That\'s wrong answer ;(.')
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))

