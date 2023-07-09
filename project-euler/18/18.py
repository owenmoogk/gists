with open('data.txt') as f:
  lines = f.readlines()

triangle = []
for line in lines:
  line = line.strip('\n')
  triangle.append(line.split(' '))

for i in range(len(triangle)):
  for j in range(i+1):
    triangle[i][j] = int(triangle[i][j])

# data is loaded into array triangle

for i in reversed(range(len(triangle)-1)):
  for itemIndex in range(len(triangle[i])):
    if triangle[i+1][itemIndex] > triangle[i+1][itemIndex+1]:
      triangle[i][itemIndex] += triangle[i+1][itemIndex]
    else:
      triangle[i][itemIndex] += triangle[i+1][itemIndex+1]

print(triangle[0][0])