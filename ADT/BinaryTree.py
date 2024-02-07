#-----------------------------------------------------
# ST1507 DSAA 
# CA2
#
# This file represents a binary tree node.
# Attributes:
#     __key: The value stored in the node.
#     __left_tree: The left subtree of the node.
#     __right_tree: The right subtree of the node.
#
#-----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : BinaryTree.py
#
#-----------------------------------------------------
# To run: python main.py
#-----------------------------------------------------

class BinaryTree:
    """
    Represents a binary tree node.

    Attributes:
        __key: The value stored in the node.
        __left_tree: The left subtree of the node.
        __right_tree: The right subtree of the node.
    """

    def __init__(self, key):
        """
        Initializes a binary tree node with the given key and optional left and right subtrees.

        Parameters:
            __key: The value to be stored in the node.
            __left_tree (BinaryTree, optional): The left subtree. Defaults to None.
            __right_tree (BinaryTree, optional): The right subtree. Defaults to None.
        """
        self.__key = key
        self.__left_tree = None
        self.__right_tree = None

    def set_key(self, key):
        """
        Sets the value of the node.

        Parameters:
            key: The value to be set.
        """
        self.__key = key

    def get_key(self):
        """
        Returns the value of the node.

        Returns:
            The value stored in the node.
        """
        return self.__key
    
    def get_left_tree(self):
        """
        Returns the left subtree of the node.

        Returns:
            The left subtree.
        """
        return self.__left_tree
    
    def get_right_tree(self):
        """
        Returns the right subtree of the node.

        Returns:
            The right subtree.
        """
        return self.__right_tree
    
    def insert_left(self, key):
        """
        Inserts a new node with the given key as the left child of the current node.

        Parameters:
            key: The value of the new node to be inserted.
        """
        if self.__left_tree == None:
            # If there is no left subtree, create a new BinaryTree node and assign it as the left subtree
            self.__left_tree = BinaryTree(key)
        else:
            # If there is already a left subtree, create a new BinaryTree node, swap it with the existing left subtree
            # and attach the existing left subtree to the new node's left subtree
            t = BinaryTree(key)
            self.__left_tree, t.__left_tree = t, self.__left_tree

    def insert_right(self, key):
        """
        Inserts a new node with the given key as the right child of the current node.

        Parameters:
            key: The value of the new node to be inserted.
        """
        if self.__right_tree == None:
            # If there is no right subtree, create a new BinaryTree node and assign it as the right subtree
            self.__right_tree = BinaryTree(key)
        else:
            # If there is already a right subtree, create a new BinaryTree node, swap it with the existing right subtree
            # and attach the existing right subtree to the new node's right subtree
            t = BinaryTree(key)
            self.__right_tree, t.__right_tree = t, self.__right_tree

    def print_in_order(self, level=0):
        """
        Prints the binary tree in reversed in-order traversal.
        It starts from the right then to the left.

        Parameters:
            level: The level of the current node in the tree. Used for indentation. Defaults to 0.

        Returns:
            A string representing the in-order traversal of the tree.
        """
        traversal_str = ''
        # Traverse right subtree first (if exists)
        if self.__right_tree:
            traversal_str += self.__right_tree.print_in_order(level + 1)
        # Add current node's key with indentation
        traversal_str += '.' * level + str(self.__key) + '\n'
        # Traverse left subtree (if exists)
        if self.__left_tree:
            traversal_str += self.__left_tree.print_in_order(level + 1)
        return traversal_str
    
    def inorder_traversal(self):
        """
        Performs an in-order traversal of the binary tree and returns the keys of the nodes in a list.

        Returns:
            list: A list containing the keys of the nodes in the binary tree in in-order traversal.
        """
        result = []  # Initialize an empty list to store the keys of the nodes
        
        # Traverse the left subtree recursively if it exists
        if self.__left_tree:
            result.extend(self.__left_tree.inorder_traversal())
        
        # Append the key of the current node to the result list
        result.append(self.__key)
        
        # Traverse the right subtree recursively if it exists
        if self.__right_tree:
            result.extend(self.__right_tree.inorder_traversal())
        
        return result
        
    def bracket_inorder_traversal(self, string=False):
        """
        Performs an in-order traversal of the binary tree and returns the keys of the nodes in a list with brackets.

        Returns:
            list: A list containing the keys of the nodes in the binary tree in in-order traversal with brackets.
        """
        if string: result = ''
        else: result = []  # Initialize an empty list to store the keys of the nodes
        
        # Traverse the left subtree recursively if it exists
        if self.__left_tree:
            if string:
                result += '(' + self.__left_tree.bracket_inorder_traversal(string)
            else:
                result.extend(['(', *self.__left_tree.bracket_inorder_traversal(string)])
        
        # Append the key of the current node to the result list
        if string:
            result += str(self.__key)
        else:
            result.append(self.__key)
        
        # Traverse the right subtree recursively if it exists
        if self.__right_tree:
            if string:
                result += self.__right_tree.bracket_inorder_traversal(string) + ')'
            else:
                result.extend([*self.__right_tree.bracket_inorder_traversal(string), ')'])
        
        return result

    def shallow_tree(self):
        """
        Returns a one level string representation of the binary tree using parentheses.

        Returns:
            A string representing the binary tree using parentheses.
        """
        if self.__left_tree and self.__right_tree:
            # If both left and right subtrees exist, recursively construct the string representation
            left = self.__left_tree.shallow_tree()
            right = self.__right_tree.shallow_tree()
            return f"({left}{self.__key}{right})"
        else:
            # If either left or right subtree is None, return the key itself
            return self.__key

    """
    OOP Principles applied

    Encapsulation:
    The BinaryTree class encapsulates attributes (__key, __left_tree, __right_tree) and 
    methods (set_key, get_key, get_left_tree, get_right_tree, insert_left, insert_right, print_in_order, shallow_tree) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the binary tree class using high-level methods like insert_left, insert_right, print_in_order, etc., 
    without needing to know the internal implementation details of these methods. They are abstracted away from the 
    complexities of managing tree nodes and pointers, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The insert_left and insert_right methods can handle different types of input (e.g., integers, strings) to create new nodes. 
    This flexibility allows users to work with various types of data seamlessly, without needing to worry about the 
    underlying implementation details.

    Modularity:
    Each method in the BinaryTree class serves a specific purpose, promoting modularity and code reusability. 
    For example, the print_in_order method is responsible for printing the binary tree in an in-order traversal, 
    while the shallow_tree method constructs a string representation of the tree using parentheses. 
    This modular design makes the class easier to understand, maintain, and extend.
    """