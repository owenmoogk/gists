# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

finaln=0
hi=str(2**1000)
for counter in range (0,302):
  a=int(hi[counter])
  finaln=finaln+a
print(finaln)