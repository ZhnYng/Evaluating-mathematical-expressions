class BinaryTree:
    """
    Represents a binary tree node.

    Attributes:
        key: The value stored in the node.
        leftTree: The left subtree of the node.
        rightTree: The right subtree of the node.
    """

    def __init__(self, key, leftTree=None, rightTree=None):
        """
        Initializes a binary tree node with the given key and optional left and right subtrees.

        Parameters:
            key: The value to be stored in the node.
            leftTree (BinaryTree, optional): The left subtree. Defaults to None.
            rightTree (BinaryTree, optional): The right subtree. Defaults to None.
        """
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey(self, key):
        """
        Sets the value of the node.

        Parameters:
            key: The value to be set.
        """
        self.key = key

    def getKey(self):
        """
        Returns the value of the node.

        Returns:
            The value stored in the node.
        """
        return self.key
    
    def getLeftTree(self):
        """
        Returns the left subtree of the node.

        Returns:
            The left subtree.
        """
        return self.leftTree
    
    def getRightTree(self):
        """
        Returns the right subtree of the node.

        Returns:
            The right subtree.
        """
        return self.rightTree
    
    def insertLeft(self, key):
        """
        Inserts a new node with the given key as the left child of the current node.

        Parameters:
            key: The value of the new node to be inserted.
        """
        if self.leftTree == None:
            # If there is no left subtree, create a new BinaryTree node and assign it as the left subtree
            self.leftTree = BinaryTree(key)
        else:
            # If there is already a left subtree, create a new BinaryTree node, swap it with the existing left subtree
            # and attach the existing left subtree to the new node's left subtree
            t = BinaryTree(key)
            self.leftTree, t.leftTree = t, self.leftTree

    def insertRight(self, key):
        """
        Inserts a new node with the given key as the right child of the current node.

        Parameters:
            key: The value of the new node to be inserted.
        """
        if self.rightTree == None:
            # If there is no right subtree, create a new BinaryTree node and assign it as the right subtree
            self.rightTree = BinaryTree(key)
        else:
            # If there is already a right subtree, create a new BinaryTree node, swap it with the existing right subtree
            # and attach the existing right subtree to the new node's right subtree
            t = BinaryTree(key)
            self.rightTree, t.rightTree = t, self.rightTree

    def printInOrder(self, level=0):
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
        if self.rightTree:
            traversal_str += self.rightTree.printInOrder(level + 1)
        # Add current node's key with indentation
        traversal_str += '.' * level + str(self.key) + '\n'
        # Traverse left subtree (if exists)
        if self.leftTree:
            traversal_str += self.leftTree.printInOrder(level + 1)
        return traversal_str
    
    def inorder_traversal(self):
        """
        Performs an in-order traversal of the binary tree and returns the keys of the nodes in a list.

        Returns:
            list: A list containing the keys of the nodes in the binary tree in in-order traversal.
        """
        result = []  # Initialize an empty list to store the keys of the nodes
        
        # Traverse the left subtree recursively if it exists
        if self.leftTree:
            result.extend(self.leftTree.inorder_traversal())
        
        # Append the key of the current node to the result list
        result.append(self.key)
        
        # Traverse the right subtree recursively if it exists
        if self.rightTree:
            result.extend(self.rightTree.inorder_traversal())
        
        return result
        
    def bracket_inorder_traversal(self, string=False):
        """
        Performs an in-order traversal of the binary tree and returns the keys of the nodes in a list.

        Returns:
            list: A list containing the keys of the nodes in the binary tree in in-order traversal.
        """
        if string: result = ''
        else: result = []  # Initialize an empty list to store the keys of the nodes
        
        # Traverse the left subtree recursively if it exists
        if self.leftTree:
            if string:
                result += '(' + self.leftTree.bracket_inorder_traversal(string)
            else:
                result.extend(['(', *self.leftTree.bracket_inorder_traversal(string)])
        
        # Append the key of the current node to the result list
        if string:
            result += str(self.key)
        else:
            result.append(self.key)
        
        # Traverse the right subtree recursively if it exists
        if self.rightTree:
            if string:
                result += self.rightTree.bracket_inorder_traversal(string) + ')'
            else:
                result.extend([*self.rightTree.bracket_inorder_traversal(string), ')'])
        
        return result

    def return_tree(self):
        """
        Returns a string representation of the binary tree using parentheses.

        Returns:
            A string representing the binary tree using parentheses.
        """
        if self.leftTree and self.rightTree:
            # If both left and right subtrees exist, recursively construct the string representation
            left = self.leftTree.return_tree()
            right = self.rightTree.return_tree()
            return f"({left}{self.key}{right})"
        else:
            # If either left or right subtree is None, return the key itself
            return self.key

    """
    OOP Principles applied

    Encapsulation:
    The BinaryTree class encapsulates attributes (key, leftTree, rightTree) and 
    methods (setKey, getKey, getLeftTree, getRightTree, insertLeft, insertRight, printInOrder, return_tree) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the binary tree class using high-level methods like insertLeft, insertRight, printInOrder, etc., 
    without needing to know the internal implementation details of these methods. They are abstracted away from the 
    complexities of managing tree nodes and pointers, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The insertLeft and insertRight methods can handle different types of input (e.g., integers, strings) to create new nodes. 
    This flexibility allows users to work with various types of data seamlessly, without needing to worry about the 
    underlying implementation details.

    Modularity:
    Each method in the BinaryTree class serves a specific purpose, promoting modularity and code reusability. 
    For example, the printInOrder method is responsible for printing the binary tree in an in-order traversal, 
    while the return_tree method constructs a string representation of the tree using parentheses. 
    This modular design makes the class easier to understand, maintain, and extend.
    """