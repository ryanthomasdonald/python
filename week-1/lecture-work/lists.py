# day1 = "Sunday"
# day2 = "Monday"
# day3 = "Tuesday"
# day4 = "Wednesday"
# day5 = "Thursday"
# day6 = "Friday"
# day7 = "Saturday"

# # C.R.U.D.

# # Create list
# # Read data from list
# # Update data in list
# # Delete data from list

# # Here's are some types of lists:

# days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] # strings

# nums = [1, 2, 3, 4, 5] # integers

# print(nums)

# nums.append(6)

# print(nums)

# An "index" is how you retrieve a value from a list.
# They are zero-based, i.e. start with "0".

# planet1 = "Earth"
# planet2 = "Jupiter"
# planet3 = "Neptune"
# planet4 = "Mars"
# planet5 = "Saturn"
# planet6 = "Mercury"
# planet7 = "Uranus"
# planet8 = "Pluto"

# planets = ["Earth", "Jupiter", "Neptune", "Mars", "Saturn", "Mercury", "Uranus", "Venus"]

# for planet in planets:
#     print(planet)

# planets.append("Pluto")

# print(planets)
# del planets[8]
# print(planets)

# print(len(planets))

# index = 0

# while index < len(planets):
#     print(planets[index].lower())
#     index += 1

# arr = []

# count = 0

# print(arr)

# while count <= 10:
#     arr.append(count)
#     count += 1

# print(arr)

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# print(todos)

# todos.append("go to the post office")

# print(todos)

# index = 0

# while index < len(todos):
#     print(f"{index + 1}. {todos[index]}")
#     index += 1

# list1 = [0, 1, 2, 3]

# # print(list1)
# # del list1[2] # how to delete items from list
# # print(list1)

# print(list1)
# del list1[1:3]
# print(list1)

# # list2 = [4, 5, 6, 7]

# # list3 = list1 + list2

# # print(list3)

# # list1.append(list2) # list (array) in a list = [0, 1, 2, 3 [4, 5, 6, 7]]

# # list1.extend(list2) # concatenates [0, 1, 2, 3, 4, 5, 6, 7]

# list1[2] = 99 # changes values in list

# print(list1)

# houston_cities = ["Katy", "Memorial City", "Sugar Land", "The Heights", "River Oaks", "Pasadena"]
# clear_lake_cities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

# # print(len(houston_cities))

# houston_cities.append("I'm Not From That Area City")
# clear_lake_cities.append("Don't Live Around Thereville")

# # print(houston_cities)
# # print(clear_lake_cities)

# houston = houston_cities + clear_lake_cities

# print(houston)

# htx1 = houston[0:4]
# htx2 = houston[2:6]
# htx3 = houston[-2:]

# print(htx1)
# print(htx2)
# print(htx3)

# houston.insert(4, "Denver")
# print(houston)

# missing_city = houston.pop(-1)
# print(missing_city)
# print(houston)

# index = houston.index("Seabrook")
# print(index)

# houston.sort()
# print(houston)

# for city in houston:
#     print(city)

# # index = 0

# while index < len(houston):
#     print(f"{index + 1} " + houston[index])
#     index += 1

# numbers = [1, 2, 3, 4, 5]

# print(numbers)
# numbers.clear() # clears list
# print(numbers)

# print(numbers)
# numbers.sort() # sorting (numerical order)
# print(numbers)

# index = numbers.index(4) # finds an index number
# print(index)

# print(numbers)
# last_num = numbers.pop() #popping and item out of list
# print(last_num)
# print(numbers)

# new_numbers = numbers[1:4] # slicing a list

# print(numbers)
# print(new_numbers)

# numbers.insert(3, 6) #insert
# print(numbers)

# Do 6-11 and 13
# 6 done
# 7 done
# 8 done
# 9 done
# 10 done
# 11 done
# 13 

# a = 4
# b = a

# print(a, b)

# b = 5

# print(a, b)

# list_a = [1, 2, 3, 4, 5]

# list_b = list_a.copy()

# print(list_a, list_b)

# list_b.append(6)

# print(list_a, list_b)

# a = 4 # 0000 (mem addr.)

# b = a # 0001 (mem addr.) # passing by reference versus value (look up)

# b = 5 # 0001 (mem addr.)

# arr = ["*"]

# arr2 = arr * 5

# print(arr2)

# tic_tac_toe = [["X", "X", "X"],
#                ["X", "O", "X"],
#                ["X", "X", "O"]]

# print(tic_tac_toe[1][1]) # first index is "row", second index is "column"

# my_string = "hello"
# print(my_string)

# # print(my_string[1:])

# index = 0

# while index < len(my_string):
#     print(my_string[index])
#     index += 1

# new_my_string = list(my_string) # converts to list
# print(new_my_string)

# updated_string = "".join(new_my_string) # converts back to string
# print(updated_string)

# reverse string
# my_string = "DigitalCrafts"
# my_string_list = list(my_string)
# reverse_list = ""

# index = 0
# while index < len(my_string):
#     reverse_list += my_string_list.pop()
#     index+=1

# print(reverse_list)

# range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(10, 20) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# range(10, 20, 2) # stepping by 2

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)

# for num in range(6, 18, 2):
#     print(num * 5)

# for minutes in range(1, 6):
#     print(minutes)
#     for seconds in range(1, 6):
#         print(seconds)

# chapters = ['Python', 'Javascript', "HTML/CSS", "Node", "React", "Redux"]

# days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

# for chapter in chapters:
#     print("")
#     print(chapter)
#     for day in days:
#         print("    " + day)

