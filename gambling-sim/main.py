import random

profit = -10000
money = 10000
currentBet = 2

wins = 0
losses = 0

while money > 0:
  if random.random() < 0.45:
    money += currentBet
    currentBet = 1
    wins += 1
    print("WIN: ", money)
  else:
    money -= currentBet
    currentBet *= 2
    losses += 1
    print("LOSE: ", money)

  if (money > 11000):
    profit += 1000
    money -= 1000

print(profit)
