#!/usr/bin/env python3


def prime(ran_number):
    k = 0
    for i in range(2, ran_number // 2 + 1):
        if (ran_number % i == 0):
            k += 1
    if (k <= 0):
        return 1
    else:
        return 0
