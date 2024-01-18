class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
        self.leftValue = None  # Additional fields to store values
        self.rightValue = None

    def setLeftValue(self, value):
        self.leftValue = value

    def getLeftValue(self):
        return self.leftValue

    def setRightValue(self, value):
        self.rightValue = value

    def getRightValue(self):
        return self.rightValue

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key
    
    def getLeftTree(self):
        return self.leftTree
    
    def getRightTree(self):
        return self.rightTree
    
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree

    def printPostorder(self, level=0):
        if self.rightTree is not None:
            self.rightTree.printPostorder(level + 1)
        print('.' * level + str(self.key))
        if self.leftTree is not None:
            self.leftTree.printPostorder(level + 1)

    def return_tree(self):
        if self.leftTree and self.rightTree:
            left = self.leftTree.return_tree()
            right = self.rightTree.return_tree()
            return f"({left}{self.key}{right})"
        else:
            return self.key