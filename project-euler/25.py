curr = 1
prev = 0
keepGoing = True
index = 1
while keepGoing:
  index += 1
  tmp = prev
  prev = curr
  curr += tmp

  if len(str(curr)) == 1000:
    print(index)
    keepGoing = False