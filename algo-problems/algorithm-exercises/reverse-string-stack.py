from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def remove(self):
        element = self.stack.pop()
        return(element)

    def size(self):
        return(len(self.stack))

def reverse_string(string):
    reverseString = Stack()
    for i in string:
        reverseString.push(i)
    returnString = ''
    while reverseString.size() > 0:
        returnString += reverseString.remove()
    return(returnString)

print(reverse_string("hello my name is owen"))