'''
Task 1: Calculate Factorial Using a Function
Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion
I'm using recursion here
'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number: "))
print("Factorial of",n,"is",factorial(n))

print('Thank you')