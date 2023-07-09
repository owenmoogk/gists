lines = []

with open('words.txt') as f:
  lines = f.readlines()


final = []
for word in lines:
  if word[2] == 'a' and word[4] == 'e' and word[0]=='s':
    final.append(word)

print(final)