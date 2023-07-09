# Given a 2D matrix, return all the elements of the matrix in a spiral order.

def spiralMatrix(array):
    returnList = []
    # initial direction
    direction = 'right'
    # getting the dimensions
    height = len(array)
    width = len(array[0])
    # setting x and y coords to 0. these are used to access the array
    x = 0 
    y = 0
    # setting the number of rotations to 1. add one every rotation around matrix
    rotations = 1
    while True:
        returnList.append(array[y][x])
        if len(returnList) >= height * width:
            break
        if direction == "right":
            x += 1
            if x == width - rotations:
                direction = 'down'
        elif direction == "left":
            x -= 1
            if x == -1 + rotations:
                direction = 'up'
        elif direction == "down":
            y += 1
            if y == height - rotations:
                direction = 'left'
        elif direction == "up":
            y -= 1
            if y == rotations:
                direction = 'right'
                rotations += 1
    return(returnList)

nums = [[1,2,3,1001],
        [8,9,4,1002],
        [7,6,5,1003],
        [111,222,333,1004],
        [10,11,12,13]]
print(spiralMatrix(nums))