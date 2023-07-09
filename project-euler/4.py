# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.




largestn=0
for y in range (1,1000):
  for x in range (1,1000):
    n=str(x*y)
    stringlength=len(n)
    slicedString=n[stringlength::-1]
    if slicedString==n:
      slicedString=int(slicedString)
      if largestn<slicedString:
        largestn=slicedString
print(largestn)