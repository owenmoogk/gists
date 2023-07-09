# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?




finalscounter = 0
biggest = 0
print('calculating')
for n in range(1,1000000):
  checkingn = n
  scounter=0
  while checkingn != 1:
    if checkingn % 2 == 0:
      checkingn = checkingn / 2
      scounter = scounter + 1
    else:
      checkingn = (3*checkingn) + 1
      scounter = scounter + 1
  if scounter > finalscounter:
    finalscounter = scounter
    biggest = n
print(biggest)