import math

numberOfPoints, circumference = list(map(int, input().split()))

points = list(map(int, input().split()))
pointsDictionary = {}
for i in points:
  if i in pointsDictionary:
    pointsDictionary[i] += 1
  else:
    pointsDictionary[i] = 1

listOfPoints = list(pointsDictionary.keys())
total = 0
for i in pointsDictionary.keys():
  firstNumber = i
  secondNumbers = {}
  for point in listOfPoints:
    if point >= firstNumber+2 and point < firstNumber+circumference/2:
      secondNumbers[point] = 0

  for secondNumber in secondNumbers.keys():
    for point in listOfPoints:
      if point >= math.floor(circumference/2+1)+i and point <= math.floor(circumference/2+1) + secondNumber:
        secondNumbers[secondNumber] += pointsDictionary[point]

  for secondNumber in secondNumbers.keys():
    total += pointsDictionary[firstNumber] * secondNumbers[secondNumber]
    
print(total)