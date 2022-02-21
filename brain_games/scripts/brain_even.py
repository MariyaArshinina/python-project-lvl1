#!/usr/bin/env python3
import prompt
from random import randint


def brain_even():
    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answers = 0
    for x in range(0, 3):
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        your_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and your_answer == 'yes':
            print('Correct!')
            right_answers += 1
        elif random_number % 2 == 0 and your_answer == 'no':
            print('"no" is wrong answer ;(. Correct answer was "yes".')
            print('Let\'s try again, {}!'.format(name))
            break
        elif random_number % 2 != 0 and your_answer == 'no':
            print('Correct!')
            right_answers += 1
        elif random_number % 2 != 0 and your_answer == 'yes':
            print('"yes" is wrong answer ;(. Correct answer was "no".')
            print('Let\'s try again, {}!'.format(name))
            break
        else:
            print('That\'s wrong answer ;(.')
            print('Let\'s try again, {}!'.format(name))
            break
        if right_answers == 3:
            print('Congratulations, {}!'.format(name))


def main():
    print('Welcome to the Brain Games!')
    brain_even()

    if __name__ == '__main__':
        main()
