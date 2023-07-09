# 18003569377 --> 1800 flowers

# given a phone number and a list of words, return a list of words that is contained within the phone number

phoneNumber = "3662277"
words = ["foo","bar","baz","cap","cat","car","emo","foobar"]

keys = {'a': '2', 'b': '2', 'c': '2',\
        'd': '3', 'e': '3', 'f': '3',\
        'g': '4', 'h': '4', 'i': '4',\
        'j': '5', 'k': '5', 'l': '5',\
        'm': '6', 'n': '6', 'o': '6',\
        'p': '7', 'q': '7', 'r': '7', 's': '7',\
        'u': '8', 't': '9', 'v': '8',\
        'w': '9', 'x': '9', 'y': '9', 'z': '9'}

def isInNumber(word, phoneNumber):
    number = ""
    for letter in word:
        number += keys[letter]
    if number in phoneNumber:
        return(True)
    return(False)

output = []
for word in words:
    if isInNumber(word, phoneNumber):
        output.append(word)

print(output)