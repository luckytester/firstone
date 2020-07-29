#!/bin/python3

def hr_if_else(n):

    n = int(input("Type a number:"))

    if n % 2 == 1 or 2 <= n <= 5 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')


hr_if_else(int(input()))