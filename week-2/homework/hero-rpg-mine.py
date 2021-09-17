class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        life = True
        if self.health <= 0:
            life = False
        return life

class Hero(Character):
    def attack(self, goblin):
        goblin.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        if goblin.health <= 0:
            print("The goblin is dead.")

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def attack(self, hero):
        hero.health -= self.power
        print(f"The goblin does {self.power} damage to you.")
        if hero.health <= 0:
            print("You are dead.")

    def print_status(self):
        print(f"The goblin has {self.health} health and {self.power} power.")

def print_title():
    print("""

It's time for...


██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
██║     ███████║██████╔╝██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   
██║     ██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
███████╗██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   

""")

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    print_title()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight goblin")
        print("2. Do nothing")
        print("3. Flee")
        user_input = input("Choice: ")
        print()
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.\n")
            break
        else:
            print(f"Invalid input: {user_input}")
            print()
        if goblin.health > 0:
            goblin.attack(hero)

main()