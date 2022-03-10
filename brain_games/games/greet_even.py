#!/usr/bin/env python3
import prompt
name = prompt.string('May I have your name?: ')


def greet_even():
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
