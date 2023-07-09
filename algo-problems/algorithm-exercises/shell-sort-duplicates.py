def shellSort(elements):
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j-gap] > anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2

if __name__ == "__main__":
    tests = [
        [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ]
    for i in tests:
        i = list(set(i))
        shellSort(i)
        print(i)