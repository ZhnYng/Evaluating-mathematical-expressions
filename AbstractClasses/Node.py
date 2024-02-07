import abc

class Node:
    """
    Base class representing a node in a linked list.
    """
    @abc.abstractmethod
    def __init__(self):
        """
        Initializes a new Node with a 'next_node' attribute set to None.
        This attribute will point to the next node in the linked list.
        """
        self.next_node = None