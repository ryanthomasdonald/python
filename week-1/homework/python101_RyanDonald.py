print("\r")
print("***))) Exercise 1 (((***") # Prints fancy titles!!!
print("\r")

cost = float(input("What is the final total of your meal? "))
service = input("Was your service good, fair, or bad? ")

if service.lower() == "good":
    tip = cost * 0.2
elif service.lower() == "fair":
    tip = cost * 0.15
elif service.lower() == "bad":
    tip = cost * 0.1
else:
    print("Please restart the calculator and provide valid answers.")
    exit()

total = cost + tip

print("Tip amount: $" + "%.2f" % tip)
print("Total amount: $" + "%.2f" % total)

print("\r")
print("***))) Exercise 2 (((***")
print("\r")

cost = float(input("What is the final total of your meal? "))
service = input("Was your service good, fair, or bad? ")
people = float(input("How many people are splitting the check? "))

if service.lower() == "good":
    tip = cost * 0.2
elif service.lower() == "fair":
    tip = cost * 0.15
elif service.lower() == "bad":
    tip = cost * 0.1
else:
    print("Please restart the calculator and provide valid answers.")
    exit()

total = cost + tip
split = total / people

print("Tip amount: $" + "%.2f" % tip)
print("Total amount: $" + "%.2f" % total)
print("Amount per person: $" + "%.2f" % split)

print("\r")
print("***))) Exercise 3 (((***")
print("\r")

coins = 0

print(f"You have {coins} coins.")

answer = input("Would you like another coin? Type 'yes' or 'no'. ")

while answer.lower() == "yes":
    coins += 1
    print(f"You have {coins} coins.")
    answer = input("Would you like another coin? Type 'yes' or 'no'. ")
print(f"Don't spend all {coins} coins in one place!")

print("\r")
print("***))) Exercise 4 (((***")
print("\r")

# I modified this to format some horizontal spaces into the box, just FYI.

print("BOX TIME!!!")
width = int(input("Width? "))
height = int(input("Height? "))
visible_height = height - 1
empty_space = (width - 2) * "  "

print("* " * width)
while visible_height - 1 > 0:
    print(f"*{empty_space} *")
    visible_height -= 1
print("* " * width)

print("\r")
print("***))) Exercise 5 (((***")
print("\r")

space = " "
star = "*"

print(f"{space * 3}" + star)
print(f"{space * 2}" + f"{star * 3}")
print(f"{space}" + f"{star * 5}")
print(f"{star * 7}")

print("\r")
print("***))) Exercise 6 (((***")
print("\r")

count = 1

while count <= 10:
    ans1 = (f"{count * 1}")
    print(str(count) + " X 1 = " + str(ans1))
    ans2 = (f"{count * 2}")
    print(str(count) + " X 2 = " + str(ans2))
    ans3 = (f"{count * 3}")
    print(str(count) + " X 3 = " + str(ans3))
    ans4 = (f"{count * 4}")
    print(str(count) + " X 4 = " + str(ans4))
    ans5 = (f"{count * 5}")
    print(str(count) + " X 5 = " + str(ans5))
    ans6 = (f"{count * 6}")
    print(str(count) + " X 6 = " + str(ans6))
    ans7 = (f"{count * 7}")
    print(str(count) + " X 7 = " + str(ans7))
    ans8 = (f"{count * 8}")
    print(str(count) + " X 8 = " + str(ans8))
    ans9 = (f"{count * 9}")
    print(str(count) + " X 9 = " + str(ans9))
    ans10 = (f"{count * 10}")
    print(str(count) + " X 10 = " + str(ans10))
    count += 1