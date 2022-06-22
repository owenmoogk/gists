import random
import matplotlib.pyplot as plt

austinLikesCoins = {
  0:0,
  1:0,
  2:0,
  3:0,
  4:0,
  5:0
}

trials = int(input("Enter the amount of trials: "))

for i in range(trials):
  counter = 0
  for i in range(5):
    win = random.randint(0,1)

    if win == 1:
      counter += 1

  austinLikesCoins[counter] += 1

sum = 0
for i in range(6):
  sum += austinLikesCoins[i]
for i in range(6):
  austinLikesCoins[i] = austinLikesCoins[i] / sum
print( austinLikesCoins)

plt.bar([0,1,2,3,4,5], list(austinLikesCoins.values()))
plt.show()