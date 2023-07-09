# given n number of stairs, and an array of possible moves, determine the number of possible ways to get up the stairs.

num = 5
possibilities = [1,3,5]

def numWays(n):
    if n == 0 or n == 1:
        return(1)
    else:
        return(numWays(n-1) + numWays(n-2))

def numWaysBottomUp(n):
    if n == 0 or n == 1:
        return(1)
    nums = list(range(n+1))
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i-1] + nums[i-2]
    return(nums[n])

def numWaysBetter(n):
    if n == 0 or n == 1:
        return(1)
    return(numWays(n-1) + numWays(n-2))

print(numWays(num))
print(numWaysBottomUp(num))