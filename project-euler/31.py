coins = [1,2,5,10,20,50,100,200]
target = 200

def solution(target, coins):
    # to solve this problem we are going to use an array to calculate first the values to make 1, all the way up to target(200)
    # first, we loop through the array as if our coins=[1], and there is exactly one way to make every possibility
    # then, the next coin is 2, and we loop through the array again
    # we are looking for values larger or = to 2, and if they are we subtract 2 and lookup how many coins are used to make that one

    # for example, lets say our array looks like [1,1,2,2,3,3], being one way to get 1, 2 ways to get 2, 2 ways to get 3, and 4 ways to get 4, and so on
    # this is just using the 1p and 2p coins

    # we can now check for 3p coins....
    # everything less than 3 is irrelevant, but we apply the algorithm at and after 3
    # 3-3 = 0, and at the 0th index we have the number one, so we add one to the third index,
    # 4-3 = 1, and at the 1st index we have the number one, so we add one to the fourth index,
    # 5-3 = 2, and at the 2nd index we have the number two, so we add two to the fifth index etc

    # each value represents the number of ways to get to the coin at that index with the current loops.
    # index 0 = 1 is a base case that just works, because if we are adding the number that we are trying to get two we are adding exactly one possiblity, which always has a delta of 0

    possibilities = [0 for i in range(target+1)]
    possibilities[0] = 1

    for coin in coins:
        for total in range(coin, target+1):
            possibilities[total] += possibilities[total-coin]

    return(possibilities[target])


if __name__ == '__main__':
    print(solution(target, coins))