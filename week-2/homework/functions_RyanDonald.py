print("\r")
print("***))) Exercise 1 (((***") # Prints fancy titles!!!
print("\r")

# Write a function "smallest" that accepts a List of numbers as an argument.
# It should return the smallest number in the List.

nums0 = [3, 54, 2, 8, 56, 1, 9]

def smallest(nums):
    nums.sort()
    return nums[0]

print(f"Here are our numbers: {str(nums0)}")
print(f"The smallest number is: {smallest(nums0)}")

# -----------------------------------

print("\r")
print("***))) Exercise 2 (((***")
print("\r")

# Write a function "largest" that accepts a List of numbers as an argument.
# It should return the largest number in the List.

nums0 = [3, 54, 2, 8, 56, 1, 9]

def largest(nums):
    nums.sort()
    return nums[-1]

print(f"Here are our numbers: {str(nums0)}")
print(f"The largest number is: {largest(nums0)}")

# -----------------------------------

print("\r")
print("***))) Exercise 3 (((***")
print("\r")

# Write a function "shortest" that accepts a list of strings as an argument.
# It should return the shortest string in the list.

strings0 = ["nylon", "rib", "auto", "chairs", "grandma"]

def shortest(strings):
    index = 1000
    for word in strings:
        if len(word) < index:
            index = len(word)
            shortest_word = word
    return shortest_word

print(f"Here are our words: {str(strings0)}")
print(f"The shortest word is: {shortest(strings0)}")

# -----------------------------------

print("\r")
print("***))) Exercise 4 (((***")
print("\r")

# Write a function "longest" that accepts a list of strings as an argument.
# It should return the longest string in the list.

strings0 = ["nylon", "rib", "auto", "grandma", "chairs"]

def longest(strings):
    index = 0
    for word in strings:
        if len(word) > index:
            index = len(word)
            longest_word = word
    return longest_word

print(f"Here are our words: {str(strings0)}")
print(f"The longest word is: {longest(strings0)}")

# -----------------------------------