# In this assignment you are going to create a TODO app. When the app starts it should present user with the following menu:

# Press 1 to add task

# Press 2 to delete task (HARD MODE)

# Press 3 to view all tasks

# Press q to quit

# The user should only be allowed to quit when they press 'q'.

# Add Task:

# Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low.

# Delete Task: (HARD MODE)

# Show user all the tasks along with the index number of each task. User can then enter the index number of the task to delete the task.

# View all tasks:

# Allow the user to view all the tasks in the following format:

# 1 - Wash the car - high

# 2 - Mow the lawn - low

# Store each task in a dictionary and use 'title' and 'priority' as keys of the dictionary.

# Store each dictionary inside an array. Array will represent list of tasks.

# ** HINT **

# tasks = [] # global array

# input("Enter your option")

#----------------------------------------------------------------------------

# Process:

# Remember C.R.U.D.

# Enter new to-do
# Store to-do in list
# Display list of to-dos
# number the items when displayed
    # allows user to select item to update or delete
    # item for the to-do list is item number minus 1 (indexing from 0)

# Prioritize:
# Make a dictionary sorted by priority

# Begining dict:
todos = {
    "high" : [],
    "medium" : [],
    "low" : []
}

app_running = True

def print_todos():
    high = todos["high"]
    medium = todos["medium"]
    low = todos["low"]
    print("High: ")
    print()
    print()

while app_running == True:
    print("""
Welcome to Task Manager™!

Enter "1" to add task.
Enter "2" to delete task.
Enter "3" to view all tasks.
Enter "q" to quit.
""")
    choice = input("Make a choice: ")

    if choice == "1":
        new_item  = input("What task would you like to add?: ")
        priority = input("How important is this task ('high', 'medium', or 'low')?: ")
        if priority.lower() == "high":
            todos["high"] = new_item
        elif priority.lower() == "medium":
            todos["medium"] = new_item
        elif priority.lower() == "low":
            todos["low"] = new_item
        else:
            print("Please input valid answers.")
    # elif choice == "2":

    # elif choice == "3":

    elif choice.lower() == "q":
        app_running = False
        print("Good luck with your day!")