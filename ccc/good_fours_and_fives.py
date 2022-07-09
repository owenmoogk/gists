import math

numberToSum = int(input())

numberOf4s = 0
numberOf5s = 0

sum = 0
while sum < numberToSum:
  numberOf5s += 1
  sum += 5

while sum > numberToSum:
  numberOf5s -= 1
  numberOf4s += 1
  sum -= 1

if numberOf5s < 0:
  print(0)

else:
  print(math.floor(numberOf5s / 4)+1)