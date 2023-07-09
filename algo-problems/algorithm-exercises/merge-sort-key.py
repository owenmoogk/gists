def mergeSortedArrays(a,b, key, descending):
    sortedList = []
    if descending:
        while len(a) > 0 and len(b) > 0:
            if a[0][key] > b[0][key]:
                sortedList.append(b[0])
                b.pop(0)
            else:
                sortedList.append(a[0])
                a.pop(0)
    else:
        while len(a) > 0 and len(b) > 0:
            if a[0][key] < b[0][key]:
                sortedList.append(b[0])
                b.pop(0)
            else:
                sortedList.append(a[0])
                a.pop(0)
    sortedList += a + b
    return(sortedList)

def mergeSort(elements, key, descending = False):
    if len(elements) == 1:
        return(elements)
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = mergeSort(left, key, descending)
    right = mergeSort(right, key, descending)

    return(mergeSortedArrays(left, right, key, descending))

if __name__ == "__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    print(mergeSort(elements, "age", True))