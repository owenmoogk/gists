# when given an array / grid of letters (2d), determine if a given word is within the grid

def searchHorizontal(board, word, x, y):
    if x + len(word) > len(board[0]):
        return(False)
    for i in range(1,len(word)):
        if word[i] == board[y][x+i]:
            pass
        else:
            return(False)
    return(True)

def searchVertical(board, word, x, y):
    if y + len(word) > len(board):
        return(False)
    for i in range(1,len(word)):
        if word[i] == board[y+i][x]:
            pass
        else:
            return(False)
    return(True)

def wordSearch(board, word):
    for x in range(0,len(board[0])):
        for y in range(0,len(board)):
            if board[y][x] == word[0]:
                if searchHorizontal(board, word, x, y) or searchVertical(board, word, x, y):
                    return(True)
    return(False)


board = [
    ["D","B","C"],
    ["O","F","C"],
    ["G","D","E"]
]
word = "DOG"
print(wordSearch(board, word))