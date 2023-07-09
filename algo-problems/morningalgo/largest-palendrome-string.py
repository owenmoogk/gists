# given a string return the length of the largest palendrome substring

def largestPalendrome(word):
    largest = 1 # the largest has to be at least 1

    # checking for ones with a single letter at center
    index = 0
    while index < len(word):
        currentLength = 1
        i = 1
        while True:
            if index-i < 0 or index + i >= len(word):
                break
            if word[index-i] == word[index+i]:
                currentLength += 2
                i += 1
            else:
                break
        if currentLength > largest:
            largest = currentLength
        index += 1

    # checking for ones with a double letter center
    index = 0
    while index < len(word)-1:
        currentLength = 0
        if word[index] == word[index+1]:
            currentLength = 2
            i = 1
            while True:
                if index-i < 0 or index+i+1 >= len(word):
                    break
                if word[index-i] == word[index+i+1]:
                    currentLength += 2
                    i += 1
                else:
                    break
        if currentLength > largest:
            largest = currentLength
        index += 1
    # return
    return(largest)

word = "wgnwiorrraceeeecarrrgnne"
print(largestPalendrome(word))