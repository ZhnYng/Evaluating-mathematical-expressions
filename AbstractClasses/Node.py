#-----------------------------------------------------
# ST1507 DSAA 
# CA2
#
# Abstract node class
#
#-----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : Node.py
#
#-----------------------------------------------------
# To run: python main.py
#-----------------------------------------------------
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