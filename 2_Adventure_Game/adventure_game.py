import time
import random

# Prints strings to console with a pause
def print_pause(s):
    print(s)
    time.sleep(2)

# Confirms user input is valid
# If not keep asking until valid input is entered
def valid_input():
    print_pause("What would you like to do? ")
    while True:
        choice = input("(Please enter 1 or 2.) ")
        if choice == '1' or choice == '2':
            break
        else:
            print_pause("Not an option. Please try again")
    return choice

#Ask user to play again if so reset game. If not, Exit game
def play_again():
    print_pause("Would you like to play again?")
    while True:
        play = input("Enter (y/n) ").lower()
        if play == 'y':
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif play == 'n':
            print("OK Goodbye!")
            exit(0)
        else:
            print_pause("Input Invalid")

# Ask user if they wish to fight or run away
def fight(weapon, enemy):
    print_pause("Would you like to (1) fight or (2) run away? ")
    choice = valid_input()
    if choice == '1':
        if weapon == "Sword":
            print_pause(f"As the {enemy} moves to attack, you unsheath your "
                        "new {weapon}.")
            print_pause(f"The {weapon} of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your shiny new "
                        "toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}. You are "
                        "victorious!")
            play_again()
        elif weapon == "Warhammer":
            print_pause(f"As the  {enemy} moves to attack, your new "
                        "{weapon} appears floating in front of you.")
            print_pause(f"The {weapon} of Ogoroth shines brightly in your "
                        "hand as you raise the {weapon} high in the air")
            print_pause(f"But the {enemy} takes one look at your shiny new "
                        "toy and and gets absorbed in the gem powering"
                        "up the Axe!")
            print_pause(f"You have rid the town of the {enemy}. "
                        "You are victorious!")
            play_again()
        elif weapon == "Axe":
            print_pause(f"As the {enemy} moves to attack, you summon "
                        "your new {weapon}.")
            print_pause(f"The {weapon} of Ogoroth breaks through the front "
                        "into your hand")
            print_pause(f"But the {enemy} takes one look at your shiny new "
                        "toy and runs away!")
            print_pause(f"you throw your axe at the {enemy} but they vanish "
                        "in thin air")
            print_pause("the axe returns to your hand")
            print_pause(f"You have rid the town of the {enemy}. "
                        "You are victorious!")
            play_again()
        else:
            print_pause("You feel a bit under-prepared for this, what with "
                        "only having a tiny dagger.")
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the troll.")
            print_pause("You have been defeated!")
            play_again()
    else:
        print_pause("You run back into the field. Luckily, you don't seem "
                    "to have been followed.")
        field(weapon, enemy)

# prints introduction of game to the screen
def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a pirate is somewhere around here, and "
                "has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")

#Events that happen inside the house
def house(weapon, enemy):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps "
                "a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    fight(weapon, enemy)

# events that happen inside the cave
def cave(weapon, enemy):
    print_pause("You peer cautiously into the cave.")
    if weapon not in ["Sword", "Axe", "Warhammer"]:
        weapon = random.choice(["Sword", "Axe", "Warhammer"])
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause(f"You discard your silly old dagger and take the "
                    "{weapon} with you.")
        print_pause("You walk back out to the field.")
        field(weapon, enemy)
    else:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(weapon, enemy)

#events that happen inside the field
def field(weapon, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    ans = valid_input()
    if ans == '1':
        house(weapon, enemy)
    elif ans == '2':
        cave(weapon, enemy)

# runs the game
def play_game():
    enemy = random.choice(["Alien", "Zombie", "Witch"])
    intro()
    weapon = "dagger"
    field(weapon, enemy)


play_game()
