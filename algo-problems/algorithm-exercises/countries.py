class Node:

    def __init__(self, data):
        self.children = []
        self.parent = None
        self.data = data

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return(level)

    def printTree(self, level = -2):
        if level == -1:
            return
        spaces = "   " * self.getLevel()
        print(spaces + self.data)
        for child in self.children:
            child.printTree(level - 1)

def buildProductTree():
    root = Node("Global")

    india = Node("India")

    gujarat = Node("Gujarat")
    gujarat.addChild(Node("Ahmedabad"))
    gujarat.addChild(Node("Baroda"))

    karnataka = Node("Karnataka")
    karnataka.addChild(Node("Bangluru"))
    karnataka.addChild(Node("Mysore"))

    india.addChild(gujarat)
    india.addChild(karnataka)

    usa = Node("USA")

    nj = Node("New Jersey")
    nj.addChild(Node("Princeton"))
    nj.addChild(Node("Trenton"))

    california = Node("California")
    california.addChild(Node("San Francisco"))
    california.addChild(Node("Mountain View"))
    california.addChild(Node("Palo Alto"))

    usa.addChild(nj)
    usa.addChild(california)

    root.addChild(india)
    root.addChild(usa)

    return root

if __name__ == "__main__":
    globalTree = buildProductTree()
    globalTree.printTree(2)
    