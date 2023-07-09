class Node:

    def __init__(self, name, designation):
        self.children = []
        self.parent = None
        self.name = name
        self.designation = designation

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

    def printTree(self, printType):
    
        spaces = "   " * self.getLevel()
        if printType == "name":
            print(spaces + self.name)
        elif printType == "role":
            print(spaces + self.designation)
        else:
            print(spaces + self.name, "("+self.designation+")")
        for child in self.children:
            child.printTree(printType)

def buildProductTree():
    infra_head = Node("Vishwa","Infrastructure Head")
    infra_head.addChild(Node("Dhaval","Cloud Manager"))
    infra_head.addChild(Node("Abhijit", "App Manager"))

    cto = Node("Chinmay", "CTO")
    cto.addChild(infra_head)
    cto.addChild(Node("Aamir", "Application Head"))

    hr_head = Node("Gels","HR Head")

    hr_head.addChild(Node("Peter","Recruitment Manager"))
    hr_head.addChild(Node("Waqas", "Policy Manager"))

    ceo = Node("Nilupul", "CEO")
    ceo.addChild(cto)
    ceo.addChild(hr_head)

    return ceo

if __name__ == "__main__":
    companyTree = buildProductTree()
    companyTree.printTree("blah")