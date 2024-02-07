# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Class representing a sorted linked list.

# Attributes:
#     __head_node (Node): Head of sorted list.
#     __length (int): Length of sorted list.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : SortedList.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------

class SortedList:
    """
    Class representing a sorted linked list.

    Attributes:
        __head_node (Node): Head of sorted list.
        __length (int): Length of sorted list.
    """

    def __init__(self):
        """
        Initializes a new SortedList
        """
        self.__head_node = None
        self.__length = 0

    def __append_to_head(self, new_node):
        """
        Private helper method to append a new node at the head of the list.

        Parameters:
            new_node: The new node to be appended.
        """
        new_node.next_node = self.__head_node  # Link new node to the current head
        self.__head_node = new_node  # Update the head to be the new node
        self.__length += 1  # Increment the __length of the list

    def insert(self, new_node):
        """
        Inserts a new node into the sorted list in the correct position.
        
        Parameters:
            new_node: The new node to be inserted.
        """
        # Handling the case where the list is empty
        if self.__head_node is None:
            self.__head_node = new_node
            self.__length += 1
            return

        # Handling the case where the new node should be the new head
        if new_node < self.__head_node:
            self.__append_to_head(new_node)
            return

        # Iterating through the list to find the correct position for the new node
        leftNode = self.__head_node
        rightNode = self.__head_node.next_node

        # Loop until the correct position for the new node is found
        while rightNode is not None:
            # Check if the new node should be inserted between leftNode and rightNode
            if new_node < rightNode:
                # Adjust pointers to insert the new node
                new_node.next_node = rightNode
                leftNode.next_node = new_node
                self.__length += 1
                return
            # Move to the next nodes for comparison
            leftNode = rightNode
            rightNode = rightNode.next_node

        # If the correct position is at the end of the list, append the new node
        leftNode.next_node = new_node
        self.__length += 1


    def items(self):
        """
        Retrieves a list of string representations of each node in the list.

        Returns:
            list: A list of string representations of nodes.
        """
        nodes = [node.__str__() for node in self.iterate()]  # List comprehension to convert each node to string
        return nodes

    def __str__(self):
        """
        Optimized __str__ method using .join instead of +=.

        Returns:
            str: A string representation of the sorted list.
        """
        nodes = [str(f"'{node}'") for node in self.iterate()]  # List comprehension to convert each node to string
        return ','.join(nodes)  # Joining all node strings with a comma

    def iterate(self):
        """
        Generator to iterate over each node in the list.

        Yields:
            object: Each node in the list.
        """
        current = self.__head_node
        while current is not None:
            yield current  # Yielding each node one by one
            current = current.next_node

    """
    OOP Principles applied

    Encapsulation:
    The SortedList class encapsulates attributes (__head_node, __length) and methods (__append_to_head, insert, items, __str__, iterate) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the sorted linked list class using high-level methods like insert, items, etc., 
    without needing to know the internal implementation details of these methods. They are abstracted away from the 
    complexities of managing linked list nodes and pointers, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The insert method can handle different types of input to insert new nodes into the list. 
    This flexibility allows users to work with various types of data seamlessly, without needing to worry about the 
    underlying implementation details.

    Modularity:
    Each method in the SortedList class serves a specific purpose, promoting modularity and code reusability. 
    For example, the insert method is responsible for inserting new nodes into the list, 
    while the items method retrieves a list of string representations of nodes. 
    This modular design makes the class easier to understand, maintain, and extend.
    """