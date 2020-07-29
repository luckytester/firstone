#!/bin/python3

try:
    n = int(input("Type a number between 1 and 100:"))
    print("\n")
except ValueError:
    print("Only integers are allowed. Please try again")    

if 1 <= n <= 100:
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
else:
    print("BETWEEN 1 AND 100, U DUMBASS!!!")

