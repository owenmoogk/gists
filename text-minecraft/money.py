from colorama import Fore, Back, Style

money = 100

def addMoney(x):
    global money
    money = money + x
    print(Fore.GREEN)
    print ("You now have",money,"dollars")
    print (Fore.WHITE)

def showMoney():
    print (Fore.GREEN)
    print ("You have",money,"dollars")
    print (Fore.WHITE)