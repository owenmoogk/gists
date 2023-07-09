from math import ceil, floor

def insertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor

        if (i+1) % 2 == 0: # if sorted list has an even amount of numbers
            median = (elements[floor(i/2)] + elements[ceil(i/2)]) / 2
            print(median)
        else:
            print(float(elements[int(i/2)]))

if __name__ == "__main__":
    elements = [2,1,5,7,2,0,5]
    insertionSort(elements)
    print(elements)