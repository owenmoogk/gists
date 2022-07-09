from cmath import inf


numberOfPeople = int(input())

personDatas = []

for i in range(numberOfPeople):
  personDatas.append(list(map(int, input().split())))

largestPosition = 0

for i in range(numberOfPeople):
  if personDatas[i][0] > largestPosition:
    largestPosition = personDatas[i][0]

def calculateWalkingTime(position, walkingSpeed, hearingDistance, concertPosition):

  if position == concertPosition:
    return 0
  if position < concertPosition and position + hearingDistance > concertPosition:
    return 0
  if position > concertPosition and position - hearingDistance < concertPosition:
    return 0

  if concertPosition > position:
    hearingDistance = -hearingDistance

  targetPosition = concertPosition + hearingDistance
  time = abs((targetPosition - position) * walkingSpeed)

  return time

smallestTime = float('inf')

i = 0
while i <= largestPosition:

  walkingTime = 0

  for person in personDatas:
    walkingTime += calculateWalkingTime(person[0], person[1], person[2], i)

  if walkingTime < smallestTime:
    smallestTime = walkingTime

  i += 1

print(smallestTime)