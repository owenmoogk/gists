numOfObservations = int(input())

class Observation():

  def __init__(self, time, distance):
    self.time = time
    self.distance = distance

observations = []

for i in range(numOfObservations):
  observation = list(map(int, input().split()))  
  observations.append(Observation(observation[0], observation[1]))

fastestSpeed = 0
for i in range(len(observations)):
  for j in range(i+1, len(observations)):
    observation1 = observations[i]
    observation2 = observations[j]
    speed = abs(observation1.distance - observation2.distance) / abs(observation1.time  - observation2.time)
    if speed > fastestSpeed:
      fastestSpeed = speed

print(fastestSpeed)