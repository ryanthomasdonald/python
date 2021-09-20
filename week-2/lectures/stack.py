# RECURSION

# It's an algorithm.
# It's a function that calls itself.

# Call Stack:
# Global frame is its native/idle state
# Functions get "stacked" on top

# class Stack():
#     def __init__(self):
#         self.data = []
#         self.length = 0
    
#     def push(self, value):
#         self.data.append(value)
#         self.length += 1

#     def pop(self):
#         if self.length == 0:
#             return None
#         removed_item = self.data.pop()
#         self.length -= 1
#         return removed_item
    
#     def peek(self):
#         if self.length == 0:
#             return None
        
#         return self.data[self.length - 1]

# stack = Stack()

# look up "balanced brackets python" (Google)

# def call_me():
#     call_me()                    # This is a "stack overflow"

# call_me()

# Recursion how-to:
# 1. Define a base case
# 2. Identify a recursive case
# 3. Return when appropriate

# Lab 1:
# Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.

def power(base, exponent):
    # base case:
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

power(2, 4) # Should equal 16

# Lab 2:
# Write a function factorial which accepts a number and returns
# the factorial of that number. A factorial is the product of an
# interger and all the integers less than the starting integer. Factorial four (4!) is
# equal to 24, because 4 * 3 * 2 * 1 equals 24. Factorial zero (0!) is always 1.

def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)

print(factorial(4))

# 1
# 1 * factorial(0) | 1 * 1 = 1
# 2 * factorial(1) | 2 * 1 = 2
# 3 * factorial(2) | 3 * 2 = 6
# 4 * factorial(3) | 4 * 6 = 24
# factorial(4)

# Lab 3:
# Write a function called recursive_range which accepts a number and adds up all
# the numbers from 0 to the number passed to the function

def recursive_range(num):
    if num == 0:
        return 0

    return num + recursive_range(num - 1)

print(recursive_range(6))

# 4. Write a recursive function called reverse which accepts
# a string and returns a new string in reverse

# 5. Write a recursive function called isPalindrome which returns
# true if the string passed to it is a palindrome (reads the same forward and backward).
# Otherwise returns false.

# 6. Write function called product_of_array which takes in
# an array of numbers and returns the product of them all