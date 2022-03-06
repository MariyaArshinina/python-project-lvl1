#!/usr/bin/env python3
import prompt
name = prompt.string('May I have your name?: ')


def greet():
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
