# given a binary tree, find the max depth
def getHeight(self):
    if self.data == None:
        return(0)
    lheight = 0
    rheight = 0
    if self.left:
        lheight = self.left.getHeight()
    if self.right:
        rheight = self.right.getHeight()

    if lheight > rheight:
        return(lheight + 1)
    else:
        return(rheight + 1)