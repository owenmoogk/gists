numberOfPoints, circumference = list(map(int, input().split()))

points = list(map(int, input().split()))
pointsDictionary = {}
for i in points:
  if i in pointsDictionary:
    pointsDictionary[i] += 1
  else:
    pointsDictionary[i] = 1

numOfResults = 0

def hasCenteredTriangle(p1, p2, p3):
  listOfPoints = [p1,p2,p3]
  listOfPoints.sort()
  if max(listOfPoints) - min(listOfPoints) <= circumference/2:
    return(False)
  listOfPoints[0] += circumference 
  if max(listOfPoints) - min(listOfPoints) <= circumference/2:
    return(False)
  listOfPoints[1] += circumference 
  if max(listOfPoints) - min(listOfPoints) <= circumference/2:
    return(False)
  return(True)

pointsDictionaryKeys = list(pointsDictionary.keys())
for i in range(len(pointsDictionaryKeys)):
  for j in range(i+1, len(pointsDictionaryKeys)):
    for k in range(j+1, len(pointsDictionaryKeys)):      
      # triangle does not encapsulate center
      if not hasCenteredTriangle(pointsDictionaryKeys[i], pointsDictionaryKeys[j], pointsDictionaryKeys[k]):
        continue
      numOfResults += pointsDictionary[pointsDictionaryKeys[i]] * pointsDictionary[pointsDictionaryKeys[j]] * pointsDictionary[pointsDictionaryKeys[k]]

print(numOfResults)