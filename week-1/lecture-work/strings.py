# strings

# "Ryan"

# 'Donald'

# "I'm a new developer."

# 'I\'ve escaped as a string using a backslash.' # shows how escape characters work (I've)

# """
# We the People of the United States, in Order to form a more perfect Union, establish 
# Justice, insure domestic Tranquility, provide for the common defence, promote the 
# general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do 
# ordain and establish this Constitution for the United States of America.
# """

# print("Hello" + "world.") # Helloworld.

# print("3" + "5") # 35 (string)

# print(3 + 5) # 8 (integer)

# print(3.14 * 2) # 6.28 (integer)

# # boolean values have a capitalized first letter
# True # 1
# False # 0

# print(True + True) # 2

# # escape character formatting
# print("""
# We the People of the United States, in Order to form a more perfect Union, establish \v\v\v
# \tJustice, insure domestic Tranquility, provide for the common defence, promote the\n\n 
# general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do 
# ordain and establish this Constitution for the United States of America.
# """)

# eight = 8

# 8 + 8

# 8 - 2

# 8.0 / 3.14

# print(8 + 3)

# first_name = "Ryan"
# last_name = "Donald"

# print(first_name, last_name) # Ryan Donald

# print(first_name + " " + last_name) #Ryan Donald

# found_coins = 20
# magic_coins = 10
# stolen_coins = 3

# result = found_coins + magic_coins * 365 - stolen_coins * 52 # 3514

# print(result)

# first_name = "Ryan"
# last_name = "Donald"

# # sentence1 = "Hello {} {}, how are you doing today?".format(first_name, last_name) # index numbers for variables start at 0
# sentence1 = "Hello {first} {last}, how are you doing today?".format(first = first_name, last = last_name) # reference to a reference
# sentence2 = "Hello {1} {0}, how are you doing today?".format(first_name, last_name) # index numbers can assign order

# print(sentence1, sentence2)

first_name = "Ryan"
last_name = "Donald"

sentence = f"Hello {first_name} {last_name}, how are you doing today?"

print(sentence)