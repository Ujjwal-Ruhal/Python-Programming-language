'''
Task 2: Using the Math Module for Calculations
Uses the math module to calculate the:
-- Square root of the number
-- Natural logarithm (log base e) of the number
-- Sine of the number (in radians)
'''

import math

def main():
    number = int(input("Enter a number: "))
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine = math.sin(number)
    print("Square root of", number, "is", square_root)
    print("Natural logarithm of", number, "is", natural_log)
    print("Sine of", number, "is", sine)

main()