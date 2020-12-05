import money
import inventory
import health
from colorama import Fore, Back, Style

print("\nYou are stuck in a video game, and you need to find a way out by collecing weapons and beating the ender dragon to free the end men. Only then will they give you a portal to let you out of their universe. \n")
print("You currently have 100 dollars. Type 'money' to show the amount of money you have\n")
print("You can also type 'inventory' to show the items in your inventory\n")
print("Type 'health' to show your health. You have 20hp at the moment\n")
playing = True


while (playing):
    playerInput = input()
    playerInput = playerInput.lower()

    if playerInput == 'health':
        health.showHealth()
    elif playerInput == 'inventory':
        inventory.showInventory()
    elif playerInput == 'money':
        money.showMoney()
    elif playerInput == 'endgame':
        playing = False