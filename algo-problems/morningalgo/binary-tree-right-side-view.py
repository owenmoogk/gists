# this was in simplelib lmao
# given a binary tree return the right side view...
# a lot of constructer code, you only need to pay attention to the one function :)
class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def rightSideView(self):
        returnList = []
        returnList.append(self.data)
        if self.right != None:
            returnList += self.right.rightSideView()
        elif self.left != None:
            returnList += self.left.rightSideView()
        return(returnList)

    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = Node(data)
        if data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = Node(data)

def removeDuplicatesFromList(array):
    array = list(dict.fromkeys(array))
    return(array)

def buildTree(elements, rootVal = 0):
    elements = removeDuplicatesFromList(elements)
    root = Node(rootVal)
    for i in range(0,len(elements)):
        root.addChild(elements[i])
    return(root)

array = [1,4,56,2,6,44]
binaryTree = buildTree(array, rootVal=5)
print(binaryTree.rightSideView())