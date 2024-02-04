from AbstractClasses import BSTNode
from ADT.BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    def __init__(self, key=None, leftTree=None, rightTree=None):
        super().__init__(key, leftTree, rightTree)

    def add(self, key:str):
        if self.key is None:  # Tree is empty
            self.key = key
        else:
            temp_new_key, temp_curr_key = key.lower(), self.key.lower() # Ignore letter cases during comparison

            if temp_new_key < temp_curr_key:
                if self.leftTree is None:
                    self.leftTree = BinarySearchTree(key)
                else:
                    self.leftTree.add(key)
            elif temp_new_key > temp_curr_key:
                if self.rightTree is None:
                    self.rightTree = BinarySearchTree(key)
                else:
                    self.rightTree.add(key)

    def findMin(self):
        current = self
        while current.leftTree is not None:
            current = current.leftTree
        return current.key

    def delete(self, key):
        if self is None:
            return self
        if key < self.key:
            if self.leftTree is not None:
                self.leftTree = self.leftTree.delete(key)
        elif key > self.key:
            if self.rightTree is not None:
                self.rightTree = self.rightTree.delete(key)
        else:
            # Node with only one child or no child
            if self.leftTree is None:
                temp = self.rightTree
                self = None
                return temp
            elif self.rightTree is None:
                temp = self.leftTree
                self = None
                return temp
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.rightTree.findMin()
            
            # Copy the inorder successor's content to this node
            self.key = temp
            
            # Delete the inorder successor
            self.rightTree = self.rightTree.delete(temp)
        return self