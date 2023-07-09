# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


multipliednum=1
finaln=0

for n in range (1,101):
  multipliednum=multipliednum*n
print(multipliednum)

multipliednum=str(multipliednum)
#multipliednum is the factorial of 100

for strnumfinder in range (0,158):
  a=int(multipliednum[strnumfinder])
  finaln=finaln+a
  print (a)
print ("The final number is", finaln)