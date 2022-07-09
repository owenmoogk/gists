height = int(input())
width = int(input())

numberOfBrushes = int(input())

brushStrokes = []

for i in range(numberOfBrushes):
  brushStrokes.append(input())

grid = [[False for i in range(width)] for j in range(height)]

for brushStroke in brushStrokes:
  
  if brushStroke[0] == 'R':
    row = grid[int(brushStroke[2])-1]
    for i in range(len(row)):
      row[i] = not row[i]

  if brushStroke[0] == 'C':
    for gridRow in grid:
      gridRow[int(brushStroke[2])-1] = not gridRow[int(brushStroke[2])-1]

totalGold = 0
for row in grid:
  for item in row:
    if item == True:
      totalGold += 1

print(totalGold)