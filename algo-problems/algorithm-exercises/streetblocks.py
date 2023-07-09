# given each street block, and the elements that are contained
# given a list of requirements, determine the block that has the shortest distance to all the items
# blocks are always arranged linearly
# no need for input checking

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    },
]
reqs = ["gym", "school", "store"]

# approach

# iterate thru each block
# in each block find max distance to required item
    # iterate thru each block, starting from og and moving one in each direction
    # for each requirement, find if it is in the block
    # if the distance is larger than the max for this block then this is the new max
# lowest max is the result

minLargestDistance = len(blocks)
minLargestDistanceIndex = -1

for blockIndex in range(0,len(blocks)):

    tempReqs = list(reqs)
    i = 0
    while i < minLargestDistance and i+blockIndex < len(blocks) and len(tempReqs) != 0:
        for req in tempReqs:
            if blocks[blockIndex+i][req]:
                tempReqs.remove(req)
            elif blocks[blockIndex-i][req]:
                tempReqs.remove(req)
        i += 1
    if i-1 < minLargestDistance:
        minLargestDistance = i-1
        minLargestDistanceIndex = blockIndex

print(minLargestDistanceIndex)