# given a chessboard (array of strings/bools), print a boolean representing weather or not a piece can reach every spot on the board

BOARD_SIZE = 8
currentBoard = [[False for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
currentBoard[0] = ["r","r","r","r","r","r","r","r"]
currentBoard[4][4] = "k"

def check(x, y):
    if currentBoard[y][x] == True:
        return(0)
    elif currentBoard[y][x] == False:
        currentBoard[y][x] = True
        return(0)
    else:
        return(1)
    # return is whether or not someone is in the way.

def checkRook(x, y):
    # going down
    for tmpY in range(y+1, BOARD_SIZE):
        returnValue = check(x, tmpY)
        if returnValue == 1:
            break

    # going up
    for tmpY in range(y-1, -1, -1):
        returnValue = check(x, tmpY)
        if returnValue == 1:
            break
    
    # going right
    for tmpX in range(x+1, BOARD_SIZE):
        returnValue = check(tmpX, y)
        if returnValue == 1:
            break

    # going right
    for tmpX in range(x-1, -1, -1):
        returnValue = check(tmpX, y)
        if returnValue == 1:
            break

def checkBishop(x, y):
    # easiest to put these in global scope... messy but it works. Then i dont have to write reset code each time
    global tmpX, tmpY
    tmpX = x
    tmpY = y

    def resetVars():
        global tmpX, tmpY
        tmpX = x
        tmpY = y

    # right down
    while True:
        tmpX += 1
        tmpY += 1
        if tmpX >= 8 or tmpY >= 8:
            break
        returnValue = check(tmpX, tmpY)
        if returnValue == 1:
            break
    resetVars()

    # right up
    while True:
        tmpX += 1
        tmpY -= 1
        if tmpX >= 8 or tmpY < 0:
            break
        returnValue = check(tmpX, tmpY)
        if returnValue == 1:
            break
    resetVars()

    # left down
    while True:
        tmpX -= 1
        tmpY += 1
        if tmpX < 0 or tmpY >= 8:
            break
        returnValue = check(tmpX, tmpY)
        if returnValue == 1:
            break
    resetVars()

    # left up
    while True:
        tmpX -= 1
        tmpY -= 1
        if tmpX < 0 or tmpY < 0:
            break
        returnValue = check(tmpX, tmpY)
        if returnValue == 1:
            break
    resetVars()

def checkPawn(x, y):
    if y == 6:
        check(x, y-1)
        check(x, y-2)
    else:
        check(x, y-1)

def checkKnight(x, y):
    xCoords = [x+1, x+2, x+2, x+1, x-1, x-2, x-2, x-1]
    yCoords = [y-2, y-1, y+1, y+2, y+2, y+1, y-1, y-2]

    for i in range(8):
        tmpX = xCoords[i]
        tmpY = yCoords[i]

        check(tmpX, tmpY)

def checkKing(x, y):
    xCoords = [x-1, x, x+1]
    yCoords = [y-1, y, y+1]

    for tmpY in yCoords:
        for tmpX in xCoords:
            check(tmpY, tmpX)

def displayBoard():
    for i in currentBoard:
        print(i)

def main():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if currentBoard[y][x] == False or currentBoard[y][x] == True:
                continue
            else:
                if currentBoard[y][x] == "r":
                    checkRook(x, y)
                elif currentBoard[y][x] == "b":
                    checkBishop(x, y)
                elif currentBoard[y][x] =="q":
                    checkRook(x, y)
                    checkBishop(x, y)
                elif currentBoard[y][x] == "k":
                    checkKing(x,y)
                elif currentBoard[y][x] == "p":
                    checkPawn(x,y)
                elif currentBoard[y][x] == "n":
                    checkKnight(x, y)

def isBoardCovered():
    for row in currentBoard:
        for item in row:
            if item == False:
                return(False)
    return(True)

main()
displayBoard()
print(isBoardCovered())