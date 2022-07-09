numOfWood = input()
woodHeights = input()
woodWidths = input()

numOfWood = int(numOfWood)

woodHeights = woodHeights.split()
woodHeights = list(map(int, woodHeights))

woodWidths = woodWidths.split()
woodWidths = list(map(int, woodWidths))

totalArea = 0
for i in range(numOfWood):
  thisArea = woodWidths[i] * (woodHeights[i] + woodHeights[i+1]) / 2
  totalArea += thisArea

print(totalArea)