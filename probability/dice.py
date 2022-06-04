import random
import matplotlib.pyplot as plt

austinLikesCoins = {}

for i in range(2,13):
  austinLikesCoins[i] = 0

trials = int(input("Enter the amount of trials: "))

for i in range(trials):

  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)

  sum = dice1 + dice2

  austinLikesCoins[sum] += 1

print (austinLikesCoins)

sum = 0
for i in range(2,13):
  sum += austinLikesCoins[i]
for i in range(2,13):
  austinLikesCoins[i] = austinLikesCoins[i] / sum

plt.bar(range(2,13), list(austinLikesCoins.values()))
plt.show()