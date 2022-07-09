# test = {
#   (1,2,3),
#   (4,6,7),
#   (2,4,6)
# }

# print((4,2,6) in test)
# x = input().split()
# x.sort()

# print(x)

# for i in range(100000):
#   print(i)

# myDict = {
#   1 : 3,
#   2:4,
#   5:2
# }

# for i in range(len(myDict.keys())):
#   print(list(myDict.keys())[i])

# owen = '12345678'
# print(owen[-3])

def getGoodSamples(notes):
  total = 0
  total += len(notes)
  for i in range(len(notes)-1):
    if notes[i] != notes[i+1]:
      total += 1
  return(total)

print(getGoodSamples('111'))