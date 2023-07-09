# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


finaln=0

for n in range (1,1001):
  finaln=finaln+(n**n)

final = ''
digitCounter = 0
for index in range (1,11):
    
    final = final + str(finaln)[len(str(finaln)) - index]
    digitCounter += 1
    if digitCounter == 10:
        break

print (final[::-1])