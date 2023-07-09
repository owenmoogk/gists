def solution():
    i = 1
    final = 0
    doStop = False

    while not doStop:

        def isPermutation (num1, num2):

            count = [0 for i in range(10)]
            num1 = str(num1)
            num2 = str(num2)

            for digit in num1:
                count[int(digit)] += 1
            for digit in num2:
                count[int(digit)] -= 1
            for item in count:
                if item != 0:
                    return False
            return True

        if isPermutation(i*2, i):
            if isPermutation(i*3, i):
                if isPermutation(i*4, i):
                    if isPermutation(i*5, i):
                        if isPermutation(i*6, i):
                            return(i)

        i += 1

if __name__ == '__main__':
    print(solution())