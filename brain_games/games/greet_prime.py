#!/usr/bin/env python3
import prompt
import random
import brain_games.games.prime


def greet_prime():
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answers = 0
    for x in range(0, 3):
        ran_number = random.randint(1, 100)
        print('Question: ' + str(ran_number))
        prime_number = brain_games.games.prime.prime(ran_number)
        your_answer = prompt.string('Your answer: ')
        if (prime_number == 1 and your_answer == 'yes') or (
                prime_number == 0 and your_answer == 'no'):
            print('Correct!')
            right_answers += 1
        else:
            print('That\'s wrong answer ;(. ')
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))
