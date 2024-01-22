class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

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

    def printInOrder(self, level=0):
        traversal_str = ''
        if self.rightTree is not None:
            traversal_str += self.rightTree.printInOrder(level + 1)
        traversal_str += '.' * level + str(self.key) + '\n'
        if self.leftTree is not None:
            traversal_str += self.leftTree.printInOrder(level + 1)
        return traversal_str

    def return_tree(self):
        if self.leftTree and self.rightTree:
            left = self.leftTree.return_tree()
            right = self.rightTree.return_tree()
            return f"({left}{self.key}{right})"
        else:
            return self.key