#!/usr/bin/env python3


def gcd(ran_num1, ran_num2):
    if ran_num1 > ran_num2:
        temp = ran_num2
    else:
        temp = ran_num1
    for i in range(1, temp + 1):
        if ((ran_num1 % i == 0) and (ran_num2 % i == 0)):
            gcd = i
    return gcd
