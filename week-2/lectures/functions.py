# Control structures we know so far: if/else, while, and for loops
# Variables are storing data

# FUNCTIONS!

# Functions are labels that store small blocks of code that can be referenced to
# perform small, repetitive actions.

# They help clean up messy, yet functional code.
# They create subroutines
### Temperature converter
### Shopping cart
### Tax calculator
### Password strength indicator

# How to define:

# greeting = "Hello world."
# =
# def greeting():               # definition
#     print("Hello world.")     # code block 

# greeting()                    # invokes (calls) function, "Hello world." prints without separate print function

# # Lab 1 + 2
# def my_name():
#     print("Ryan Donald")

# my_name()

# # Lab 3
# # Reduce following code:

# # print("Day 1: Students in SRE class")
# # print("lecture: git 101")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")
# # print("Day 2: Students in SRE class")
# # print("lecture: git 102")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")
# # print("Day 3: Students in SRE class")
# # print("lecture: python 101")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")

# def print_names():
#     print("Students: " + "Shu", "Thomas", "Gustavo", "Alim")

# print("")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_names()

# print("")

# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_names()

# print("")

# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_names()

# print("")

# Difference between loop and function
# Loop is a control structure, cannot be called at will, runs and stops
# Functions are at your beck and call. You decide what they do and when/how often they run
# Functions can also be nested and call other functions

# Passing parameters (arguments) to functions:
# def calc(num1, num2):      # num1 = 4, num2 = 5
#     print(num1 + num2)     # prints sum of 4 and 5 (9)

# calc(4, 5)                 # prints "9"

# def print_my_name(first_name, last_name):
#     print(f"My name is {first_name} {last_name}.")

# print_my_name("Ryan", "Donald")

# Lab 4
# def person1(first_name, last_name):
#     print(first_name + last_name)

# def person2(first_name, last_name):
#     print(first_name + last_name)

# def rec_letter(my_first_name, my_last_name, rec_first_name, rec_last_name):
#     print(f"""{my_first_name} {my_last_name}
# 1234 Park St
# Anytown, Pennsylvania 12345

# April 14, 2019

# ABC College Admission’s Board
# 1234 Butler Ave
# Everywhere, CA 12345

# Dear ABC College Admission’s Board:

# My name is {my_first_name} {my_last_name}. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {rec_first_name} {rec_last_name}’s teacher for the past three. I have also been {rec_first_name}’s advisor on the science academic team here at school. Due to his qualifications, I feel that {rec_first_name} would be an excellent addition to your school.

# While he has been a student here, {rec_first_name} has always challenged himself academically, taking all of the AP courses that our school has to offer. He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# {rec_first_name} would bring much to your school, both in and out of the classroom. If you have any questions regarding {rec_first_name}’s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# Sincerely,


# {my_first_name} {my_last_name}
# Science Department Head
# Park Town High School
# """)
# rec_letter("Ryan", "Donald", "Brian", "McDonald")

# Order of arguments pushed into the function matters, just FYI.

# # Calculating an average
# def average_of_4_nums(num1, num2, num3, num4):
#     total = num1 + num2 + num3 + num4
#     average = total / 4
#     print(f"The average of these four numbers is {average}.")

# average_of_4_nums(23, 345, -44, 1)

# Again: FUNCTIONS ARE SUBROUTINES!

# This return statement completes the subroutine, but doesn't print anything. Note the syntax.
# Result of function is now stored in memory, ready to be used.
# Call stack for running functions is LIFO.
# def add(num1, num2):
#     sum = num1 + num2
#     return sum         # <-- proper syntax

# def return_3_values():
#     return 5, 10, 15                 # local variables

# num1, num2, num3 = return_3_values   # global variables
# print(num1, num2, num3)

# def add(num1 = 1, num2 = 2): #syntax for default values if no arguments are passed to function parameters

# "Return" acts as a break statement ("early return")
# def say_hello(name):
#     print(f"Hello {name}.")
#     return
#     print("XYZ")             # doesn't print

# # Temp. Converter
# # F to C
# def conv_to_celcius(f):
#     c = (f - 32) * (5 / 9)
#     print(f"Celcius: {c}")

# # C to F
# def conv_to_fahrenheit(c):
#     f = (c * 1.8) + 32
#     print(f"Fahrenheit: {f}")

# # Main program
# conv_to_celcius(32)
# conv_to_fahrenheit(0)

# Scope - Global vs. Local (lecture slides have a lot of good info)
# a = 4                      # a and b are global variables
# b = 5

# def calc(num1, num2):      # num1 and num2 are local variables
#     print(num1 + num2)

# # Tax Calc.
# tax_rate = .09  # 9 percent tax
# cost_per_small_widget = 5.00
# cost_per_large_widget = 8.00

# def calculate_cost(num_of_small_widgets, num_of_large_widgets):
#     sub_total = (num_of_small_widgets * cost_per_small_widget) + (num_of_large_widgets * cost_per_large_widget)
#     tax_amount = sub_total * tax_rate
#     total_cost = sub_total + tax_amount
#     return total_cost

# print(calculate_cost(4, 5))

