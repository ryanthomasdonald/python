import json

with open('todo.json', 'r') as fh:
    todos = json.load(fh)

def print_todos():
    for key, val in todos.items():
        print(f"{key.upper()} PRIORITY:")
        index = 0
        for task in val:
            print(f"{index + 1}: {val[index]}")
            index += 1
        print("")

def invalid_input():
    print("\nInvalid input. Get it together!")

def print_your_day():
        print("""

__  __                    ____             
\ \/ /___  __  _______   / __ \____ ___  __
 \  / __ \/ / / / ___/  / / / / __ `/ / / /
 / / /_/ / /_/ / /     / /_/ / /_/ / /_/ / 
/_/\____/\__,_/_/     /_____/\__,_/\__, /  
                                  /____/   """)

def print_add_task():
            print("""
    ___       __    __   ___     ______           __  
   /   | ____/ /___/ /  /   |   /_  __/___ ______/ /__
  / /| |/ __  / __  /  / /| |    / / / __ `/ ___/ //_/
 / ___ / /_/ / /_/ /  / ___ |   / / / /_/ (__  ) ,<   
/_/  |_\__,_/\__,_/  /_/  |_|  /_/  \__,_/____/_/|_|  
                                                        """)

def print_remove_task():
    print("""
    ____                                    ___     ______           __  
   / __ \___  ____ ___  ____ _   _____     /   |   /_  __/___ ______/ /__
  / /_/ / _ \/ __ `__ \/ __ \ | / / _ \   / /| |    / / / __ `/ ___/ //_/
 / _, _/  __/ / / / / / /_/ / |/ /  __/  / ___ |   / / / /_/ (__  ) ,<   
/_/ |_|\___/_/ /_/ /_/\____/|___/\___/  /_/  |_|  /_/  \__,_/____/_/|_|  
                                                                         """)

def print_task_manager():
    print("""

$$$$$$$$\                  $$\             $$\      $$\                                                             TM
\__$$  __|                 $$ |            $$$\    $$$ |                                                            
   $$ | $$$$$$\   $$$$$$$\ $$ |  $$\       $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
   $$ | \____$$\ $$  _____|$$ | $$  |      $$\$$\$$ $$ | \____$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
   $$ | $$$$$$$ |\$$$$$$\  $$$$$$  /       $$ \$$$  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
   $$ |$$  __$$ | \____$$\ $$  _$$<        $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      
   $$ |\$$$$$$$ |$$$$$$$  |$$ | \$$\       $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
   \__| \_______|\_______/ \__|  \__|      \__|     \__| \_______|\__|  \__| \_______| \____$$ | \_______|\__|      
                                                                                      $$\   $$ |                    
                                                                                      \$$$$$$  |                    
                                                                                       \______/                     """)

print("""

Welcome to...""")

print_task_manager()

app_running = True

while app_running == True:

    print("""
    __  ___      _          __  ___                
   /  |/  /___ _(_)___     /  |/  /__  ____  __  __
  / /|_/ / __ `/ / __ \   / /|_/ / _ \/ __ \/ / / /
 / /  / / /_/ / / / / /  / /  / /  __/ / / / /_/ / 
/_/  /_/\__,_/_/_/ /_/  /_/  /_/\___/_/ /_/\__,_/  
                                                   
Please select one of the following options:

- Type "add" to add a task.
- Type "remove" to remove a task.
- Type "view" to view all tasks.
- Type "quit" to close the program.
""")

    choice = input("What would you like to do?: ")
    if choice == "add":
        print_add_task()
        new_item = input("What task would you like to add?: ")
        add_priority = input("\nOf what importance is this task? 'High', 'Medium', 'Low'?: ").lower()
        if add_priority == 'high' or add_priority == 'medium' or add_priority == 'low':
            todos[add_priority].append(new_item)
            print(f'\n"{(new_item)}" added to "{add_priority} priority"!')
        else:
            invalid_input()
    elif choice == "remove":
        print_remove_task()
        print_todos()
        rem_priority = input("Which priority level is your task ('High', 'Medium', 'Low')? ").lower()
        if rem_priority == 'high' or rem_priority == 'medium' or rem_priority == 'low':
            item_to_del = int(input("\nInput the number of the task you'd like to remove: "))
            if item_to_del == 0:
                invalid_input()
            elif item_to_del > len(todos[rem_priority]):
                invalid_input()
            elif item_to_del <= len(todos[rem_priority]):
                print(f'\n"{todos[rem_priority][item_to_del - 1]}" removed from "{rem_priority} priority"!')
                del todos[rem_priority][item_to_del - 1]
        else:
            invalid_input()
    elif choice == "view":
        print_your_day()
        print_todos()
    elif choice == "quit":
        app_running = False
        print("\n\nThank you for using...")
        print_task_manager()
        print("\n\nYour changes are saved, so you can always come back to add new tasks or remove completed tasks.")
        print("\n\n***))) GOOD LUCK WITH YOUR DAY!!! (((***\n\n")
    else:
        invalid_input()

with open('todo.json', 'w') as fh:
    json.dump(todos, fh)