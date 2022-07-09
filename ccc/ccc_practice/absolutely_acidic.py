numberOfSensors = int(input())

readings = {}

for i in range(numberOfSensors):
  reading = int(input())
  if reading in readings.keys():
    readings[reading] += 1
  else:
    readings[reading] = 1


highestFrequency = 0
numsWithHighestFrequency = []

secondHighestFrequency = 0
numsWithSecondHighestFrequency = []

for key in readings:

  if readings[key] > highestFrequency:
    numsWithSecondHighestFrequency = numsWithHighestFrequency.copy()
    secondHighestFrequency = highestFrequency
    highestFrequency = readings[key]
    numsWithHighestFrequency = [key]

  elif readings[key] == highestFrequency:
    numsWithHighestFrequency.append(key)

  elif readings[key] > secondHighestFrequency:
    secondHighestFrequency = readings[key]
    numsWithSecondHighestFrequency = [key]

  elif readings[key] == secondHighestFrequency:
    numsWithSecondHighestFrequency.append(key)


if len(numsWithHighestFrequency) > 2:
  # get the largest abs value
  largestNumber = 0
  smallestNumber = float('inf')

  for i in numsWithHighestFrequency:
    if i > largestNumber:
      largestNumber = i
    if i < smallestNumber:
      smallestNumber = i
  
  print(largestNumber-smallestNumber)

elif len(numsWithHighestFrequency) == 2:
  print(abs(numsWithHighestFrequency[0]-numsWithHighestFrequency[1]))

elif len(numsWithHighestFrequency) == 1:
  largestNumber = numsWithHighestFrequency[0]

  largestAbsValue = 0

  for i in numsWithSecondHighestFrequency:
    if abs(largestNumber-i) > largestAbsValue:
      largestAbsValue = abs(largestNumber-i)

  print(largestAbsValue)