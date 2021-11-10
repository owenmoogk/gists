from colorama import Fore, Back, Style
from pathlib import Path
import pickle
# setting root = to current folder
root = Path(".")
inventoryData = root / "data"/"inventory.dat"

inventory = pickle.load(open(inventoryData, "rb"))

def showInventory():
    invKeys = []
    for key in inventory.keys(): 
        invKeys.append(key)
    print ()
    for i in invKeys:
        print (Fore.RED+i+':',inventory[i])
    print (Fore.WHITE)

def addToInv(item, number):
    if item in inventory:
        inventory[item] += number
        print("+"+str(number),item)
    else:
        inventory[item] = number
        print("+"+str(number),item)
    pickle.dump(inventory, open(inventoryData, "wb"))