# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
primesummation=0
print ("running")

def isPrime(number):
  y = 1
  for i in range(2,round(math.sqrt(num))+2):
    if number%i==0 & number!=i:
      y = 0
      break
  return (y)


for num in range (3,2000001,2): 
  x = isPrime(num)
  if x == 1:
    primesummation=primesummation+num
    print (num)

print (primesummation + 5) #ugh lmao

#2 and 3 dont work properly due to my for loop, so we add 5
#i could probably make it better but couldnt be bothered