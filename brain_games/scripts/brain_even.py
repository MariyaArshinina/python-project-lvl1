#!/usr/bin/env python3
import prompt
def welcome_user():
    name = prompt.string('May I have your name?:')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

def main():
    print('Welcome to the Brain Games!')
    welcome_user()


    if __name__ == '__main__':
        main()
