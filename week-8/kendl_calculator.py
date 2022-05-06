#============================================
# Title: Exercise 8.3
# Author: Professor Krasso
# Date: 05 May 2022
# Modified By: Laura Kendl
# Description: This program demonstrates the
# use of Python with calculator functions.
# Resources:
# [Ref A] W3schools: https://www.w3schools.com/python/python_functions.asp (Python Functions)
# [Ref B] Professor Krasso: Exercise 8.3 Instructions
# [Ref C] Stackoverflow: https://stackoverflow.com/questions/65949325/how-do-you-fix-missing-module-docstringpylintmissing-module-docstring (How do you fix "Missing module docstringpylint(missing-module-docstring)")
# ===========================================

"""
Provides some arithmetic functions
"""
# Create an add function and return the total.
def add(num1, num2): # "Def" creates a function in python. [Ref A]
    """Add two numbers""" # This docstring fixes Pylint error C0116. [Ref C]
    return num1 + num2

# Create a subtract function and return the subtracted total.
def subtract(num1, num2):
    """Subtract two numbers"""
    return num1 - num2

# Create a divide function and return the divided total.
def divide(num1, num2):
    """Divide two numbers"""
    return num1 / num2

# Call add function and print.
print(add(1, 2)) # [Ref B]

# Call subtract function and print.
print(subtract(4, 1))

# Call divide function and print.
print(divide(8, 2))