class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        life = True
        if self.health <= 0:
            life = False
        return life

class Larry(Character):
    def attack(self, alien):
        alien.health -= self.power
        print(f"You do {self.power} damage to the alien.")
        if alien.health <= 0:
            print("The alien is dead.")

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

class Alien(Character):
    def attack(self, larry):
        larry.health -= self.power
        print(f"The alien does {self.power} damage to you.")
        if larry.health <= 0:
            print("You are dead.")

    def print_status(self):
        print(f"The alien has {self.health} health and {self.power} power.")

def print_title():
    print('''

It's time for...


   ██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
   ██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
   ██║     ███████║██████╔╝██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   
   ██║     ██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
   ███████╗██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   


    Somewhere, in the outer reaches of deep space, a janitor named Larry could count down
the days to retirement on one hand.

    "It's hard to believe I've got less than a week left," Larry muttered to himself while
finishing one last mop of the mess hall.
    
    While he enjoyed having the base almost completely to himself, there was something
about being this close to the end that made him wonder how things would've turned out if
he'd made it all the way through The Academy. Still, he had a level of job security most
folks this far out into space could only dream of. And only a few days of it left to boot.

    He did have a bit of company though: His robot pal, Rusty. Larry had grown fond of his
agency-appointed helper, so much so that he even named it. Rusty was definitely outdated,
but that didn't matter to Larry. He enjoyed the familiarity of "Trusty Rusty" and the robot
reminded him of a time when things seemed to move a little bit slower. Maintaining an older
robot also helped pass the time and Larry figured that if his buddy had made it this far,
he may very well be indestructable.

    "Well, I guess that's it for the year, Rusty," said Larry.
    
    "01010100 01101001 01101101 01100101 00100000 01100110 01101111 01110010 00100000 
01100001 00100000 01100011 01101111 01101100 01100100 00100000 01101111 01101110 01100101
00100001 00100001 00100001," Rusty beeped.
    
    "Boy is it ever! I'll head over to the Officer's Quarters and see if they left any
bottles of suds behind in the fridge. That sure was one hell of a party..."

    The best part about being the senior janitor was that Larry's keycard granted him full
access to the entire base. (Another alien specimen exploded in the lab you say? "Someone go
find Larry." Someone puked in the anti-gravity chamber again? "Say no more! Larry's on it!")
The Officer's Quarters were all the way on the other side of the facility, so Larry headed
over that way while Rusty stayed behind to straighten up their neck of the woods.

    As he was making his way down one of the now-dimly-lit corridors, a dark figure in the
distance startled Larry something fierce.

    "Hey! Who's that?!?", shouted Larry.

    "Huh? Oh... It's me, Dave!"

    Dave was one of the medics at the base and a good friend of Larry's. A welcomed sight,
for sure.

    "Terribly sorry about that, bud," said Dave. "They must've turned the lights out to save
power over the break. I guess I overslept and missed the shuttle. Damn... Well anyway, what
are you doing all the way out here? I thought they closed this wing down before the party..."

    "I'm headed over to the Officer's Quarters to see if they left any beers in that mini-
fridge that they think is a secret."

    "Yeah, they aren't foolin' anyone... But aren't you worried about them finding out? The
security cameras are still on and that constitutes as stealing from an officer," Dave noted.

    "What are they gonna do, fire me?"

    "Good point, Larry. Let's go find some beers and drink to your retirement."

    The old pals made their way up the hill and quipped back and forth about how much nicer
the accomodations were on this side of the base (for agency standards, at least). Larry's
keycard saved the day yet again and sure enough
''')

def main():
    larry = Larry(10, 5)
    alien = Alien(6, 2)

    print_title()

    while alien.alive() and larry.alive():
        larry.print_status()
        alien.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight alien")
        print("2. Do nothing")
        print("3. Flee")
        user_input = input("Choice: ")
        print()
        if user_input == "1":
            larry.attack(alien)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.\n")
            break
        else:
            print(f"Invalid input: {user_input}")
            print()
        if alien.health > 0:
            alien.attack(larry)

main()