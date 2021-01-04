from colorama import Fore, Back, Style

inventory = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

def showInventory():
    invKeys = []
    for key in inventory.keys(): 
        invKeys.append(key)
    print ()
    for i in invKeys:
        print (Fore.RED+i+':',inventory[i])
    print (Fore.WHITE)def addToInv(item, number):
    if item in inventory:
        inventory[item] += number
        print("+"+str(number),item)
    else:
        inventory[item] = number
        print("+"+str(number),item)
    pickle.dump(inventory, open(inventoryData, "wb"))