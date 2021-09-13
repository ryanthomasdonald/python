print("\r")
print("***))) Exercise 1 (((***") # Prints fancy titles!!!
print("\r")

# First solution w/o loops:
# num_set0 = [2, 4, 5]
# num_set1 = [2, 3, 6]

# product0 = num_set0[0] * num_set1[0]
# product1 = num_set0[1] * num_set1[1]
# product2 = num_set0[2] * num_set1[2]

# final_products = [product0, product1, product2]
# print(num_set0, " X ", num_set0, " = ", final_products)

# Loop solution:
num_set0 = [2, 4, 5]
num_set1 = [2, 3, 6]
final_products = []

for i in range(len(num_set0)):
    product = num_set0[i] * num_set1[i]
    final_products.append(product)

print(num_set0, " X ", num_set0, " = ", final_products)

# -----------------------------------

print("\r")
print("***))) Exercise 2 (((***")
print("\r")

# First solution w/o loops:
nums0 = [[1, 3],
         [2, 4]]
nums1 = [[5, 2],
         [1, 0]]

sum0 = nums0[0][0] + nums1[0][0]
sum1 = nums0[0][1] + nums1[0][1]
sum2 = nums0[1][0] + nums1[1][0]
sum3 = nums0[1][1] + nums1[1][1]

final_sums_top = [sum0, sum1]
final_sums_bottom = [sum2, sum3]

# Prints proper formatting:
print(final_sums_top)
print(final_sums_bottom)

# # Loop solution:
# nums0 = [[1, 3],
#          [2, 4]]
# nums1 = [[5, 2],
#          [1, 0]]
# sums = []
#
# for x_index in range(len(nums0)):
#     nums2 = []
#     for y_index in range(len()):
#         nums2 = .append

# print("\r")
# print("***))) Exercise 3 (((***")
# print("\r")

# for i in range():

# -----------------------------------

print("\r")
print("***))) Exercise 4 (((***")
print("\r")

duplicates = [1, 4, 4, 7, 7, 3, 9, 7, 2]
no_duplicates = []

print(duplicates)

for num in duplicates:
    if num not in no_duplicates:
        no_duplicates.append(num)

print(no_duplicates)

# -----------------------------------

print("\r")
print("***))) Exercise 5 (((***")
print("\r")

# What needs to happen

# 1. Declare string in "paragraph" 
# 2. Define normal alphabet (not needed)
# 3. Define leet alphabet (not needed)
# 4. Check each letter in paragraph against normal alphabet
# 5. If in normal alphabet, transfer to "new_paragraph"
# 6. If in leetspeak, convert to leet then transfer to "new_paragraph"
# 7. Stop loop once original "paragraph" has been converted
# 8. Print Leetspeak conversion.

# Edge case: What about punctuation, etc.? (not needed in this solution)

paragraph = "The age of my dog is technically eight, but that's almost sixty in dog years."
# alphabet = ["b", "c", "d", "f", "h", "j", "k", "l", "m", "n", "p", "q", "r", "u", "v", "w", "x", "y", "z"]
# leetabet = ["4", "3", "6", "1", "0", "5", "7"]
new_paragraph = ""

print("Original: " + paragraph)
print("")

for letter in paragraph:
    leet = letter
    if leet.lower() == "a":
        leet = "4"
    elif leet.lower() == "e":
        leet = "3"
    elif leet.lower() == "g":
        leet = "6"
    elif leet.lower() == "i":
        leet = "1"
    elif leet.lower() == "o":
        leet = "0"
    elif leet.lower() == "s":
        leet = "5"
    elif leet.lower() == "t":
        leet = "7"
    new_paragraph += leet

print("Leetspeak: " + new_paragraph)

# -----------------------------------

print("\r")
print("***))) Exercise 6 (((***")
print("\r")

word = input("Type a lowercase word: ")

word = word.lower()

word = word.replace("aa", "aaaaa")
word = word.replace("ee", "eeeee")
word = word.replace("ii", "iiiii")
word = word.replace("oo", "ooooo")
word = word.replace("uu", "uuuuu")
word = word.replace("yy", "yyyyy")

print("")
print("Say it with me now: " + word)

# -----------------------------------

# print("\r")
# print("***))) Exercise 7 (((***")
# print("\r")

# # Step 1:

# message = "your refridgerator is running"
# alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
# rot13 = "nopqrstuvwxyzabcdefghijklm"
# step = 13
# encrypt = ""

# print("Your message: " + message)

# for i in range(len(message.lower())):
#     rot13 = alphabet.index[i] + step
#     encrypt += rot13

# print("Encrypted message: " + encrypt)

print("\r")
print("***))) EXERCISE 7 GUESSING GAME!!! (((***")
print("\r")

# I had a bit of trouble trying to solve this with it being so early in the class, but I figured
# it couldn't hurt to take the working code and modify it slightly to make a fun game. :)

# 1. Define encrypted statement.
# 2. Create empty variable for decrypted statement.
# 3. Define standard alphabet.
# 4. Print encrypted statement.
# 5. Print explanation of shifting.
# 6. Ask user how many characters to shift and assign the answer to a variable.
# 7. Perform decryption using shift number input (here's the loop...)
# 8. Print "decryption" and ask the user if it makes sense.
# 9. If so, print signoff message.
# 10. If not, loop until message is successfully decrypted, then print signoff message (#9).

print("Howdy! I'm Decrypt-O-Bot™!")
print("""

        \_/
       (_**)   - "Beep!"
      __) #__
     ( )...( )    ___ 
     || | | ||   |ABC|
     || | | ( )=<|XYZ|
     /\(___)      ¨¨¨
    _-'''''''-_
    ¨-,,,,,,,-¨

""")
print("Today, I'll be helping you decrypt this phrase:")
print("")
print('"' + "Lbh zhfg hayrnea, jung lbh unir yrnearq." + '"')
print("")
print("""The cypher works like this: Every letter has been shifted forward in the alphabet by the same
number of steps. Your job is to guess how many steps the phrase has been shifted using a number
between 1 and 25. Then, I'll do the hard work of translating your guess and displaying the
result. If you're unhappy with the result, I'll keep working with you until we get it right! (I
mean, I AM a robot after all...)""")
print("")
offset = int(input("Let's get started! Take a guess as to the number of shifts (1-25): "))
print("")

secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''
repeat = "n"

while repeat != "y":
    repeat = ""
    result = ""
    for char in secret:
        ascii_code = ord(char)
        is_uppercase = ascii_code >= 65 and ascii_code <= 90
        char = char.lower()
        if char not in alphabet:
            new_char = char
        else:
            idx = alphabet.find(char)
            new_idx = idx + offset
            if new_idx > 25:
                new_idx = new_idx - 26
            new_char = alphabet[new_idx]
            if is_uppercase:
                new_char = new_char.upper()
        result += new_char
    print("***VARIOUS ROBOT NOISES***")
    print("")
    print('"' + result + '"')
    print("")
    repeat = input("Does this make sense (Y/N)? ")
    if repeat.lower() == "y":
        print("")
        print("""Glad I could help! Thanks for trusting Decrypt-O-Bot™ with your sensitive 
information. We promise it won't be used against you in the coming robot 
uprising. Have a great day!!!""")
    else:
        repeat = "n"
        print("")
        offset = int(input("Sorry about that... Guess a different number (1-25): "))
        print("")