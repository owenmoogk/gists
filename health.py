from colorama import Fore, Back, Style

health = 20

def showHealth():
    print (Fore.MAGENTA)
    print ('Health:',health)
    print (Fore.WHITE)

def addHealth(num):
    health += num
    print (Fore.MAGENTA)
    print ('Your health is now',health)
    print (Fore.WHITE)