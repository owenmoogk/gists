# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


stop = 0
primeCounter = 0
number = 1
print('running')

def isPrime(num):
  y = 'prime'
  for i in range(2,num):
    if (num % i) == 0:
      y = 'not prime'
      break
  return (y)

while stop == 0:
  number += 1
  x = isPrime(number)
  if x == "prime":
    primeCounter += 1
  if primeCounter >= 10001:
    stop = 1
    print (primeCounter, number)