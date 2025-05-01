# Assignment-3:  Functions & Modules in Python
## Task 1:  Calculate Factorial Using a Function 

Factorial:
for example, the factorial of 4 (written as 4!) is equal to 1*2*3*4=24.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

Eg-
1!=1
2!=2*1
3!=3*2*1
4!=4*3*2*1
5!=5*4*3*2*1
6!=6*5*4*3*2*1
7!=7*6*5*4*3*2*1
8!=8*7*6*5*4*3*2*1
9!=9*8*7*6*5*4*3*2*1
10!=10*9*8*7*6*5*4*3*2*1

like that..

# Task 2:Using the Math Module for Calculations

Uses the math module to calculate the:
-- Square root of the number
-- Natural logarithm (log base e) of the number
-- Sine of the number (in radians)

note- 
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.log()	Returns the natural logarithm of a number
math.sin()	Returns the sine of a number in radians
import math
x = 25
print(math.isqrt(x))
print(math.log(x))
print(math.sin(x))

Like that..