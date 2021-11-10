import time
import inventory

# the intro for when the player first enters the overworld
def overworldIntro():
    print("You lie in a forign world with nothing.")
    print("Your goal? To gather resources to sustain yourself, and be prepared for anything.")
    print("Around you, there is some trees, on a dirt landscape. Off in the distance you see a cave.")
    print("Type mine to see what resources you can gather.")
    print("Type goto to see what places you can walk towards.")

# changing player locations
def goto(location):
    if location == "land":
        print("You can go to: ")
        for i in locations:
            if i != location:
                print("  -",i)
        result = input()
        result = result.upper()
        if result == "Y":
            zombieFight()
            return(caves)

# giving options to what to mine
def mine(location):
    matList = []
    if location == "land":
        matList = landMaterials
    elif location == "caves":
        matList = cavesMaterials
    print("You can mine:")
    for i in matList:
        print("  -",i)
    print ("Type your choice")
    choice = input()
    
    # checking that the choice is valid
    validChoice = False
    for i in matList:
        if choice == i:
            validChoice = True
            break
    if validChoice == False:
        print("Invalid choice")
        return
    else:
        print("how many would you like to mine?")
        numberToMine = int(input())
        print("mining",numberToMine, choice)
        mining = True
        i = 0
        while mining:
            time.sleep(1)
            inventory.addToInv(choice,1)
            i += 1
            if i >= numberToMine:
                break

            
            

    
    


# def zombieFight():


locations = ["land", "caves"]

cavesMaterials = ["stone","iron"]
landMaterials = ["wood", "dirt"]