def convertToBinary(number):
    binaryNumber = ''
    while number > 0:
        binaryNumber = str(number%2) + binaryNumber
        number = int(number/2)
    return(int(binaryNumber))

print(convertToBinary(15))