from ADT.BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    """
    Represents a binary search tree, which is a specialized type of binary tree.
    This binary search tree also has the functionalities of an AVL tree to keep it balanced.
    References: https://www.programiz.com/dsa/avl-tree

    Inherits from BinaryTree class.

    Attributes:
        key: The value stored in the node.
        leftTree: The left subtree of the node.
        rightTree: The right subtree of the node.
        height: The height of the node in the tree.
    """

    def __init__(self, key=None, leftTree=None, rightTree=None):
        """
        Initializes a binary search tree node with the given key and optional left and right subtrees.

        Parameters:
            key: The value to be stored in the node. Defaults to None.
            leftTree (BinarySearchTree, optional): The left subtree. Defaults to None.
            rightTree (BinarySearchTree, optional): The right subtree. Defaults to None.
        """
        super().__init__(key, leftTree, rightTree)
        self.__height = 1

    # Getter
    def get_height(self):
        return self.__height
    
    # Setter
    def set_height(self, height):
        self.__height = height

    def add(self, key):
        """
        Adds a new key to the binary search tree.

        Parameters:
            key: The value of the new key to be added.
        """
        if self.key is None:
            self.key = key
            return
        self.__add(key) # Recursively adds a new key to the binary search tree.
        self.__height = 1 + max(self.__get_height(self.leftTree), self.__get_height(self.rightTree)) # Calculate the height between left and right tree
        self.__balance_tree() # Check if tree requires balancing
    
    def __add(self, key):
        """
        Recursively adds a new key to the binary search tree.

        Parameters:
            key: The value of the new key to be added.
        """
        temp_key, temp_curr_key = key.lower(), self.key.lower() # Ignore letter cases during sorting/comparison
        if temp_key < temp_curr_key: # If new key is less than the current key, insert into the left tree
            if self.leftTree is None: # If tree has not been created, create one and set key as initial key
                self.leftTree = BinarySearchTree(key)
            else:
                self.leftTree.__add(key) # If tree has been created, traverse down left-wards until left tree is not found
        elif temp_key > temp_curr_key: # If new key is more than the current key, insert into the right tree
            if self.rightTree is None: # If tree has not been created, create one and set key as initial key
                self.rightTree = BinarySearchTree(key)
            else:
                self.rightTree.__add(key) # If tree has been created, traverse down right-wards until right tree is not found

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
        if key < self.key: # If key is less than current key traverse the left tree
            if self.leftTree is not None: # If the left tree exists, recursively call the delete function
                self.leftTree = self.leftTree.delete(key)
        elif key > self.key: # If key is more than current key traverse the right tree
            if self.rightTree is not None: # If the right tree exists, recursively call the delete function
                self.rightTree = self.rightTree.delete(key)
        else:
            if self.leftTree is None: # If the left tree does not exists, return the right tree
                return self.rightTree
            elif self.rightTree is None: # If the right tree does not exists, return the left tree
                return self.leftTree

            temp = self.rightTree.find_min() # Find the minimum key in the right tree.
            self.key = temp # Set current key to the minimum key in the right tree.
            self.rightTree = self.rightTree.delete(temp) # Recursively call the delete function on the right tree

        if self is not None: # If current tree exists
            self.__height = 1 + max(self.__get_height(self.leftTree), self.__get_height(self.rightTree)) # Update the height of the tree after deletion
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
        return self.__get_height(node.leftTree) - self.__get_height(node.rightTree) # Just gets the height difference between the left and right trees of the given node/tree

    def __rotate_right(self, y):
        """
        Performs a right rotation on the given node in the binary search tree.

        Parameters:
            y: The node on which the rotation is to be performed.

        Returns:
            BinarySearchTree: The root of the subtree after rotation.
        """
        x = y.leftTree # Assign x as the left subtree of y
        T2 = x.rightTree # Assign T2 as the right subtree of x

        x.rightTree = y # Assign right tree of x to y
        y.leftTree = T2 # Assign left tree of y to T2

        y.__height = 1 + max(self.__get_height(y.leftTree), self.__get_height(y.rightTree)) # Update heights after rotation
        x.__height = 1 + max(self.__get_height(x.leftTree), self.__get_height(x.rightTree)) # Update heights after rotation

        return x # Return x as the parent of y where y is in the right subtree of x

    def __rotate_left(self, x):
        """
        Performs a left rotation on the given node in the binary search tree.

        Parameters:
            x: The node on which the rotation is to be performed.

        Returns:
            BinarySearchTree: The root of the subtree after rotation.
        """
        y = x.rightTree # Assign y as the right subtree of x
        T2 = y.leftTree # Assign T2 as the left subtree of y

        y.leftTree = x # Assign left tree of y to x
        x.rightTree = T2 # Assign right tree of x to T2

        x.__height = 1 + max(self.__get_height(x.leftTree), self.__get_height(x.rightTree)) # Update heights after rotation
        y.__height = 1 + max(self.__get_height(y.leftTree), self.__get_height(y.rightTree)) # Update heights after rotation

        return y # Return y as the parent of x where x is in the left subtree of y

    def __balance_tree(self):
        """
        Balances the binary search tree if it becomes unbalanced after an insertion or deletion operation.

        Returns:
            BinarySearchTree: The root of the balanced binary search tree.
        """
        balance = self.__balance_factor(self) # Gets current balance factor

        if balance > 1: # If balance factor is above threshold of 1
            if self.__balance_factor(self.leftTree) < 0:  # If balance factor of left tree is less than 0 perform a left-right rotation
                self.leftTree = self.__rotate_left(self.leftTree) # Rotate the left tree to the left
            return self.__rotate_right(self) # Rotate the left tree to the right
        if balance < -1: # If balance factor is below threshold of -1
            if self.__balance_factor(self.rightTree) > 0: # If balance factor of right tree is more than 0 perform a right-left rotation
                self.rightTree = self.__rotate_right(self.rightTree) # Rotate the right tree to the right
            return self.__rotate_left(self) # Rotate the right tree to the left
        return self

    def find_min(self):
        """
        Finds the minimum key in the binary search tree.

        Returns:
            str: The minimum key found in the tree.
        """
        current = self 
        while current.leftTree is not None: # While left tree exists, keep traversing left-wards
            current = current.leftTree # This is because the left tree contains the smallest value
        return current.key

    """
    OOP Principles applied

    Encapsulation:
    The BinarySearchTree class encapsulates attributes (key, leftTree, rightTree, height) and 
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