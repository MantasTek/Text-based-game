# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:55:10 2024

@author: Mantas
"""

# Aventyr spel
# setting beggining score and room
score = 0
room = "bassement"

# Introduction text explaining the game's goal
print("Welcome to our short adventure where your score is impacted by your choices.")
print("In order to be victoriuos you need to score 80 points or more")
# we make a while loop with requirements that must be met in order to finish the game.
while room != "Exit" and score <= 80:
# Display current room and options
    print("\nYou are in the", room)
    print("Your current score is:", score)
    print("1 = Hall")
    print("2 = Pantry")
    print("3 = Kitchen")
    print("4 = Living room")
    print("5 = Bedroom")
    print("6 = Bathroom")
    print("7 = Porch")
    print("8 = Exit")
# Used to make user give us input
    choice = input("Choose where to go next (1-7): ")
# with each choice points either are given or taken
# after that player is sent to corresponding room
    if choice == "1":
        print("This is the beggining")
        score += 5
        room = "Hall"
    elif choice == "2":
        print("You found door handle on the floor")
        score += 15
        room = "Pantry"
    elif choice == "3":
        print("Bad time for snacking! We are on ther mission!")
        score -= 15
        room = "Kitchen"
    elif choice == "4":
        print("Nicely handeled! Keep on going.")
        score += 20
        room = "Living room"
    elif choice == "5":
        print("Good choice! Chance for a nap")
        score += 15
        room = "Bedroom"
    elif choice == "6":
        print("You should not have taken a shower")
        score -= 10
        room = "Bathroom"
    elif choice == "7":
        print("Do not leave the house!")
        score -= 10
        room = "Porch"
    elif choice == "8":
        score -= 30
        room = "Exit"
        break
# if player enters invalid number we set up else statement
    else:
        print("Invalid choice. Please try again.")

# Game end message and final score.
print("Did you win ?", score)

