numberOfNotes, highestNote, goodSamplesRequired = list(map(int, input().split()))

def getGoodSamples(string):
  total = 0
  total += len(string)
  for i in range(len(string)-1):
    if string[i] != string[i+1]:
      total += 1
  return(total)

def add1(string):
  myList = list(string)
  i = -1
  if '1' not in string:
    return(False)
  if myList[i] == '1':
    myList[i] = '2'
    return("".join(myList))
  if myList[i] == '2':
    while myList[i] != '1':
      myList[i] = '1'
      i -= 1
    myList[i] = '2'
    return(''.join(myList))

def createString(length):
  string = ""
  for i in range(length):
    string += "1"
  return(string)

string = createString(numberOfNotes)

while True:
  if getGoodSamples(string) == goodSamplesRequired:
    print(" ".join(string))
    break
  string = add1(string)
  if string == False:
    print(-1)
    break