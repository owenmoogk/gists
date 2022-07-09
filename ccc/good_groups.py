x = int(input())
pairsMustBeTogether = set()
for i in range(x):
  tmp = input().split()
  tmp.sort()
  pairsMustBeTogether.add(tuple(tmp))

y = int(input())
pairsMustBeSeperate = set()
for i in range(y):
  tmp = input().split()
  tmp.sort()
  pairsMustBeSeperate.add(tuple(tmp))

g = int(input())
groups = []
for i in range(g):
  tmp = input().split()
  tmp.sort()
  groups.append(tuple(tmp))

seperationViolations = 0
for currGroup in groups:

  if (currGroup[0], currGroup[1]) in pairsMustBeTogether:
    pairsMustBeTogether.remove((currGroup[0], currGroup[1]))
  if (currGroup[0], currGroup[1]) in pairsMustBeSeperate:
    seperationViolations += 1

  if (currGroup[0], currGroup[2]) in pairsMustBeTogether:
    pairsMustBeTogether.remove((currGroup[0], currGroup[2]))
  if (currGroup[0], currGroup[2]) in pairsMustBeSeperate:
    seperationViolations += 1

  if (currGroup[1], currGroup[2]) in pairsMustBeTogether:
    pairsMustBeTogether.remove((currGroup[1], currGroup[2]))
  if (currGroup[1], currGroup[2]) in pairsMustBeSeperate:
    seperationViolations += 1

print(len(pairsMustBeTogether) + seperationViolations)