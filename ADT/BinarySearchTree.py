#-----------------------------------------------------
# ST1507 DSAA 
# CA2
#
# Represents a binary search tree, which is a specialized type of binary tree.
# This binary search tree also has the functionalities of an AVL tree to keep it balanced.
# References: https://www.programiz.com/dsa/avl-tree
#
# Inherits from BinaryTree class.
#
# Attributes:
#     key: The value stored in the node.
#     left_tree: The left subtree of the node.
#     right_tree: The right subtree of the node.
#     height: The height of the node in the tree.
#
#-----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : BinarySearchTree.py
#
#-----------------------------------------------------
# To run: python main.py
#-----------------------------------------------------

from ADT.BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    """
    Represents a binary search tree, which is a specialized type of binary tree.
    This binary search tree also has the functionalities of an AVL tree to keep it balanced.
    References: https://www.programiz.com/dsa/avl-tree

    Inherits from BinaryTree class.

    Attributes:
        key: The value stored in the node.
        left_tree: The left subtree of the node.
        right_tree: The right subtree of the node.
        height: The height of the node in the tree.
    """

    def __init__(self, key=None):
        """
        Initializes a binary search tree node with the given key and optional left and right subtrees.

        Parameters:
            key: The value to be stored in the node. Defaults to None.
            left_tree (BinarySearchTree, optional): The left subtree. Defaults to None.
            right_tree (BinarySearchTree, optional): The right subtree. Defaults to None.
        """
        super().__init__(key)
        self.__height = 1

    # Getter
    def get_height(self):
        return self.__height
    
    def get_key(self):
        return self._BinaryTree__key

    def get_left_tree(self):
        return self.left_tree

    def get_right_tree(self):
        return self.right_tree
    
    # Setter
    def set_height(self, height):
        self.__height = height

    def set_key(self, key):
        self._BinaryTree__key = key

    def set_left_tree(self, left_tree):
        self.left_tree = left_tree

    def set_right_tree(self, right_tree):
        self.right_tree = right_tree

    def add(self, key):
        """
        Adds a new key to the binary search tree.

        Parameters:
            key: The value of the new key to be added.
        """
        if self._BinaryTree__key is None:
            self._BinaryTree__key = key
            return
        self.__add(key) # Recursively adds a new key to the binary search tree.
        self.__height = 1 + max(self.__get_height(self.left_tree), self.__get_height(self.right_tree)) # Calculate the height between left and right tree
        self.__balance_tree() # Check if tree requires balancing
    
    def __add(self, key):
        """
        Recursively adds a new key to the binary search tree.

        Parameters:
            key: The value of the new key to be added.
        """
        temp_key, temp_curr_key = key, self._BinaryTree__key
        if temp_key < temp_curr_key: # If new key is less than the current key, insert into the left tree
            if self.left_tree is None: # If tree has not been created, create one and set key as initial key
                self.left_tree = BinarySearchTree(key)
            else:
                self.left_tree.__add(key) # If tree has been created, traverse down left-wards until left tree is not found
        elif temp_key > temp_curr_key: # If new key is more than the current key, insert into the right tree
            if self.right_tree is None: # If tree has not been created, create one and set key as initial key
                self.right_tree = BinarySearchTree(key)
            else:
                self.right_tree.__add(key) # If tree has been created, traverse down right-wards until right tree is not found

    def delete(self, key):
        """
        Deletes a key from the binary search tree.

        Parameters:
            key: The key to be deleted.

        Returns:
            BinarySearchTree: The root of the updated binary search tree after deletion.
        """
        if self is None:
            return None

        # Recursion to find the key to be deleted
        if key < self._BinaryTree__key: # If key is less than current key traverse the left tree
            if self.left_tree is not None: # If the left tree exists, recursively call the delete function
                self.left_tree = self.left_tree.delete(key)
        elif key > self._BinaryTree__key: # If key is more than current key traverse the right tree
            if self.right_tree is not None: # If the right tree exists, recursively call the delete function
                self.right_tree = self.right_tree.delete(key)
        else:
            if self.left_tree is None: # If the left tree does not exists, return the right tree
                return self.right_tree
            elif self.right_tree is None: # If the right tree does not exists, return the left tree
                return self.left_tree

            temp = self.right_tree.find_min() # Find the minimum key in the right tree.
            self._BinaryTree__key = temp # Set current key to the minimum key in the right tree.
            self.right_tree = self.right_tree.delete(temp) # Recursively call the delete function on the right tree

        if self is not None: # If current tree exists
            self.__height = 1 + max(self.__get_height(self.left_tree), self.__get_height(self.right_tree)) # Update the height of the tree after deletion
            return self.__balance_tree() # Check if balancing is required

    def __get_height(self, node):
        """
        Calculates the height of a node in the binary search tree.

        Parameters:
            node: The node whose height is to be calculated.

        Returns:
            int: The height of the node.
        """
        if node is None:
            return 0
        return node.__height # Just gets the height of the given node

    def __balance_factor(self, node):
        """
        Calculates the balance factor of a node in the binary search tree.

        Parameters:
            node: The node whose balance factor is to be calculated.

        Returns:
            int: The balance factor of the node.
        """
        if node is None:
            return 0
        return self.__get_height(node.left_tree) - self.__get_height(node.right_tree) # Just gets the height difference between the left and right trees of the given node/tree

    def __rotate_right(self, y):
        """
        Performs a right rotation on the given node in the binary search tree.

        Parameters:
            y: The node on which the rotation is to be performed.

        Returns:
            BinarySearchTree: The root of the subtree after rotation.
        """
        x = y.left_tree # Assign x as the left subtree of y
        T2 = x.right_tree # Assign T2 as the right subtree of x

        x.right_tree = y # Assign right tree of x to y
        y.left_tree = T2 # Assign left tree of y to T2

        y.__height = 1 + max(self.__get_height(y.left_tree), self.__get_height(y.right_tree)) # Update heights after rotation
        x.__height = 1 + max(self.__get_height(x.left_tree), self.__get_height(x.right_tree)) # Update heights after rotation

        return x # Return x as the parent of y where y is in the right subtree of x

    def __rotate_left(self, x):
        """
        Performs a left rotation on the given node in the binary search tree.

        Parameters:
            x: The node on which the rotation is to be performed.

        Returns:
            BinarySearchTree: The root of the subtree after rotation.
        """
        y = x.right_tree # Assign y as the right subtree of x
        T2 = y.left_tree # Assign T2 as the left subtree of y

        y.left_tree = x # Assign left tree of y to x
        x.right_tree = T2 # Assign right tree of x to T2

        x.__height = 1 + max(self.__get_height(x.left_tree), self.__get_height(x.right_tree)) # Update heights after rotation
        y.__height = 1 + max(self.__get_height(y.left_tree), self.__get_height(y.right_tree)) # Update heights after rotation

        return y # Return y as the parent of x where x is in the left subtree of y

    def __balance_tree(self):
        """
        Balances the binary search tree if it becomes unbalanced after an insertion or deletion operation.

        Returns:
            BinarySearchTree: The root of the balanced binary search tree.
        """
        balance = self.__balance_factor(self) # Gets current balance factor

        if balance > 1: # If balance factor is above threshold of 1
            if self.__balance_factor(self.left_tree) < 0:  # If balance factor of left tree is less than 0 perform a left-right rotation
                self.left_tree = self.__rotate_left(self.left_tree) # Rotate the left tree to the left
            return self.__rotate_right(self) # Rotate the left tree to the right
        if balance < -1: # If balance factor is below threshold of -1
            if self.__balance_factor(self.right_tree) > 0: # If balance factor of right tree is more than 0 perform a right-left rotation
                self.right_tree = self.__rotate_right(self.right_tree) # Rotate the right tree to the right
            return self.__rotate_left(self) # Rotate the right tree to the left
        return self

    def find_min(self):
        """
        Finds the minimum key in the binary search tree.

        Returns:
            str: The minimum key found in the tree.
        """
        current = self 
        while current.left_tree is not None: # While left tree exists, keep traversing left-wards
            current = current.left_tree # This is because the left tree contains the smallest value
        return current._BinaryTree__key

    """
    OOP Principles applied

    Encapsulation:
    The BinarySearchTree class encapsulates attributes (key, left_tree, right_tree, height) and 
    methods (add, delete, find_min, __get_height, __balance_factor, __rotate_right, __rotate_left, __balance_tree) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the binary search tree class using high-level methods like add, delete, find_min, etc., 
    without needing to know the internal implementation details of these methods. They are abstracted away from the 
    complexities of managing tree nodes and pointers, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The add method can handle different types of input to add new keys to the tree. 
    This flexibility allows users to work with various types of data seamlessly, without needing to worry about the 
    underlying implementation details.

    Modularity:
    Each method in the BinarySearchTree class serves a specific purpose, promoting modularity and code reusability. 
    For example, the add method is responsible for adding new keys to the tree, 
    while the find_min method finds the minimum key in the tree. 
    This modular design makes the class easier to understand, maintain, and extend.
    """