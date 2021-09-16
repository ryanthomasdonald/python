# dictionary_name = {
#     "I'm a key" : "I'm a value",
#     "square_of two" : 4,              # proper syntax
#     "month" : "September",
#     "I'm true" : True
# }

# for key in dictionary_name.keys():    # prints individual keys ("key" is just a standard variable)
#     print(key)

# for val in dictionary_name.values():  # prints individual values ("val" is just a standard variable)
#     print(val)

# for key, val in dictionary_name.items():    # prints separate keys and values use ".items()"")
#     print(f"Key: {key}, Value: {val}")

# results = dictionary_name.items()     # key and value pairs are returned as tuples
# print(results)

# # Remember C.R.U.D.

# # retrieving value using key, always use quotes
# dictionary_name["hello"]
# dictionary_name["month"]

# # .get() method (or function) safely checks if items actually exist
# dictionary_name.get("what")     # returns value of "None", doesn't totally crash your program

# # Lab 1
# zodiac = {
#     "Aries" : "The Warrior",
#     "Taurus" : "The Builder",
#     "Gemini" : "The Messenger",
#     "Cancer" : "The Mother",
#     "Leo" : "The King",
#     "Virgo" : "The Analyst",
#     "Libra" : "The Judge",
#     "Scorpio" : "The Magician",
#     "Sagittarius" : "The Gypsy",
#     "Capricorn" : "The Father",
#     "Aquarius" : "The Thinker",
#     "Pisces" : "The Mystic"
# }

# print(zodiac["Taurus"])

# print(zodiac.get("other"))    # prints "None"

# result = "other" in zodiac
# print(result)                 # prints "False" (boolean)

# # How to update an item in a dic.
# zodiac["Taurus"] = "The Builder (this is me)"    # same syntax as adding
# print(zodiac["Taurus"])

# # .keys() and .values()
# print(zodiac.keys())     # loops can be used on both
# print(zodiac.values())

# # adding key/value pair
# dictionary_name["I'm a key"] = "I'm a value"     # same syntax as updating

# # deleting
# del dictionary_name["month"]

# # Lab 2
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict["Elizabeth"])

# phonebook_dict["Kareem"] = "938-489-1234"

# del phonebook_dict["Alice"]

# phonebook_dict["Bob"] = "968-345-2345"

# for name, number in phonebook_dict.items():
#     print(f"{name}: {number}")

# Dictionaries can be nested/contain nesting
# You can use index numbers to refer to nested lists in dictionaries
# See lecture presentation for further notes

# Lab 3
# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#         {
#             'name': 'Jasmine',
#             'email': 'jasmine@yahoo.com',
#             'interests': ['photography', 'tennis']
#         },
#         {
#             'name': 'Jan',
#             'email': 'jan@hotmail.com',
#             'interests': ['movies', 'tv']
#         }
#     ]
# }

# print(ramit["email"])

# print(ramit["interests"][0])

# print(ramit["friends"][0]["email"])

# print(ramit["friends"][1]["interests"][1])

#-----------------------------------------------------

# File I/O

# userID: htx
# password: coders

# # Writing to a file
# file_handler = open("hello.txt", "w")   # "w" = write
# file_handler.write("text kajhsdfkfjdfs\nsakhfjbnawe\njklnwarefg\nrjfhgbre")
# file_handler.close()

# # Reading a file
# file_handler = open("preamble.txt", "r")    # "r" = read
# contents = file_handler.read()
# file_handler.close()
# print(contents)

# # Memory Leaks

# # opens, reads, and closes file automatically:
# with open('hello.txt', 'r') as file_handler:
#     contents = file_handler.read()
#     print(contents)

# Pickle Files

# import pickle

# data = {
#     "first_name" : "Ryan",
#     "last_name" : "Donald"
# }

# # with open("data.pickle", "wb") as file_handler:
# #     pickle.dump(data, file_handler)

# import pickle

# with open("data.pickle", "r") as file_handler:
#     data = pickle.load(file_handler)
#     print(data["first_name"])                    # prints from predefined dictionary named "data" (see above)

# JSON works exactly the same way

# Lab 4

# Caching (to cache, weird spelling)

# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:

# >>>letter_histogram(‘banana’)
# {‘a’: 3, ‘b’: 1, ‘n’: 2}

# def letter_histogram(word):
#     histogram = {}
#     for letter in word:
#         if letter in histogram:
#             histogram[letter] += 1
#         else:
#             histogram[letter] = 1
#     return histogram

# print(letter_histogram("banana"))

# Write a word_histogram function that takes a paragraph of
# text as its input, and returns a dictionary containing
# the tally of how many times each word in the alphabet was
# used in the text. For example:

# >>> word_histogram('To be or not to be')   ['To', 'be', 'or', 'not', 'to', 'be']

# def word_histogram(phrase):
#     lower_phrase = phrase.lower()
#     split_phrase = lower_phrase.split()
#     new_dict = {}
#     for word in split_phrase:
#         if word in new_dict:
#             new_dict[word] += 1
#         else:
#             new_dict[word] = 1
#     return new_dict

# print(word_histogram("To be or not to be"))