#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

finaln=0

#checking if # is divisible by 5 or 3
for checkingn in range (1,1000):
    if checkingn%3==0 or checkingn%5==0:
        finaln=finaln+checkingn

#printing final number
print(finaln)