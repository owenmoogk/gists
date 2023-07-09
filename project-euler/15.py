def recursion(x, y):
    # this solution is using a recursive method which takes a base case and counts possibilities from there
    # this takes way too long so we should find a better method.

    if x == 0 or y == 0:
        return 1
    else:
        return(solution(x-1, y) + solution(x, y-1))

def backwardCoords(x, y):
    # this solution starts by making an 2d array of points, and works backwards to solve for the point at the top left
    y += 1
    x += 1

    grid = [[0 for i in range(x)] for j in range(y)]

    # each side both bottom and right have a base case of 1
    for i in range(x):
        grid[y-1][i] = 1
        grid[i][x-1] = 1

    for xUpdater in reversed(range(x-1)):
        for yUpdater in reversed(range(y-1)):
            # here we just add the two possibilities of the two forks, and apply them to that grid
            grid[xUpdater][yUpdater] = grid[xUpdater+1][yUpdater] + grid[xUpdater][yUpdater+1]

    return(grid)

if __name__ == '__main__':
    print(backwardCoords(20,20))