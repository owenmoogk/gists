# imports
import money, inventory, health
import pickle, random
import overworld
from colorama import Fore, Back, Style

# intro
print("\nYou are stuck in a video game, and you need to find a way out by collecing weapons and beating the ender dragon to free the end men. Only then will they give you a portal to let you out of their universe. \n")
print("You currently have 100 dollars. Type 'money' to show the amount of money you have")
print("You can also type 'inventory' to show the items in your inventory")
print("Type 'health' to show your health. You have 20hp at the moment\n")
print("If at any time you are done playing, just type 'endgame'")

# names
print("Enter your name to start:")
name = input()
overworld.overworldIntro()

# data
dimension = "overworld"
location = "land"

# main input checking
def getInput(input):

    # wasnt recognizing as global, /shrug
    global dimension, location

    # lowercase
    input = input.lower()

    # playerdata
    if playerInput == 'health' or playerInput == "hp":
        health.showHealth()
    elif playerInput == 'inventory' or playerInput == "inv":
        inventory.showInventory()
    elif playerInput == 'money':
        money.showMoney()

    # actions
    elif playerInput == "goto":
        if dimension == "overworld":
            location = overworld.goto(location)
    elif playerInput == "mine":
        if dimension == "overworld":
            overworld.mine(location)
    
    # kill it
    elif playerInput == 'endgame':
        playing = False

    # unknown
    else:
        print("unknown input, try again")

# main loop
playing = True
while playing:
    playerInput = input()
    getInput(playerInput)
    