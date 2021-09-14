import json

with open('todo.json', 'r') as fh:
    todos = json.load(fh)

def print_todos():
    print("""

__  __                    ____             
\ \/ /___  __  _______   / __ \____ ___  __
 \  / __ \/ / / / ___/  / / / / __ `/ / / /
 / / /_/ / /_/ / /     / /_/ / /_/ / /_/ / 
/_/\____/\__,_/_/     /_____/\__,_/\__, /  
                                  /____/   """)
    for key, val in todos.items():
        print(f"{key.upper()} PRIORITY:")
        index = 0
        for task in val:
            print(f"{index + 1}: {val[index]}")
            index += 1
        print("")

print("""

Welcome to...


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
- Type "delete" to delete a task.
- Type "view" to view all tasks.
- Type "quit" to quit.
""")

    choice = input("What would you like to do?: ")
    if choice == "add":
        new_item = input("\nWhat task would you like to add?: ")
        priority = input("\nHow important is this task? 'High', 'Medium', 'Low'?: ").lower()
        if priority == 'high' or priority == 'medium' or priority == 'low':
            todos[priority].append(new_item)
            print("\nList updated!")
        else:
            print("You did not choose a valid priority. Pleae prioritize your life!")
    if choice == "delete":
        print_todos()
        which_priority = input("What priority level is your item?\n Enter one of the following: 'High', 'Medium', 'Low' ").lower()
        item_to_del = int(input("What would you like to check off or delete? "))
        print(f"{todos[which_priority][item_to_del - 1]} deleted!")
        del todos[which_priority][item_to_del - 1]
    if choice == "view":
        print_todos()
    if choice == "quit":
        app_running = False
        print("Good luck with your day! Come back to check things off or add items!")
        
with open('todo.json', 'w') as fh:
    json.dump(todos, fh)