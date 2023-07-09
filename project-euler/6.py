# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



sumofnumbers=0
totalofsqrednums=0
for n in range (1,101):
  sumofnumbers=sumofnumbers+n
sqrsumofnumbers=sumofnumbers*sumofnumbers
print("The SQRT of the sum of numbers is,",sqrsumofnumbers)

for s in range (1,101):
  totalofsqrednums=totalofsqrednums+(s*s)
print("The total of SQRED NUMS is,",totalofsqrednums)


finalans=sqrsumofnumbers-totalofsqrednums
print(finalans)