import random
import matplotlib.pyplot as plt

austinLikesCoins = {
  0:0,
  1:0,
  2:0,
  3:0,
  4:0
}

trials = int(input("Enter the amount of trials: "))

for i in range(trials):
  counter = 0
  for i in range(4):
    dice = random.randint(0,1)

    if dice == 1:
      counter += 1

  austinLikesCoins[counter] += 1

print (austinLikesCoins)

plt.plot([0,1,2,3,4], list(austinLikesCoins.values()))
plt.show()