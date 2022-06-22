import random
import matplotlib.pyplot as plt

austinLikesCoins = {}

for i in range(51):
  austinLikesCoins[i] = 0

trials = int(input("Enter the amount of trials: "))

for i in range(trials):
  counter = 0
  for i in range(50):
    dice = random.randint(0,1)

    if dice == 1:
      counter += 1

  austinLikesCoins[counter] += 1

sum = 0
for i in range(51):
  sum += austinLikesCoins[i]
for i in range(51):
  austinLikesCoins[i] = austinLikesCoins[i] / sum
print( austinLikesCoins)

plt.bar(list(range(51)), list(austinLikesCoins.values()))
plt.show()