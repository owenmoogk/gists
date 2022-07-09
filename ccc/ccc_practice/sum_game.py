numberOfGames = int(input())

firstTeamScoring = list(map(int, input().split()))
secondTeamScoring = list(map(int, input().split()))

totalFirstTeam = 0
totalSecondTeam = 0

result = 0

for i in range(numberOfGames):
  totalFirstTeam += firstTeamScoring[i]
  totalSecondTeam += secondTeamScoring[i]

  if totalFirstTeam == totalSecondTeam:
    result = i+1

print(result)