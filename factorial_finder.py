def factorial_finder(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*factorial_finder(n-1)

try:
    n = int(input("Please, insert a number to obtain his factorial: "))
except ValueError:
    print("Only integers are allowed. Please try again")

if n < 0:
    print("Sorry, there's no factorial for a negative number...")
else:
    print(f"The factorial of {n} is {factorial_finder(n)}.")

if __name__=="__main__":
    factorial_finder(n)
