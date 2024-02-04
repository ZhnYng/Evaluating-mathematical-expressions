class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.__items = []  # Initialize a private list to store items in the stack.

    # Getter
    def get_items(self):
        """
        Get the items in the stack.
        """
        return self.__items  # Return the private list of items.
    
    # Setter
    def set_items(self, items):
        """
        Get the items in the stack.
        """
        self.__items = items  # Set the private list of items.

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        return len(self.__items) == 0  # Check if the length of the stack is 0.

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        - item: The item to be added to the stack.
        """
        self.__items.append(item)  # Append the item to the end of the list.

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
        - item: The item from the top of the stack.
        
        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():  # Check if the stack is not empty.
            return self.__items.pop()  # Remove and return the last item from the list.
        else:
            raise IndexError("Popping from an empty stack")  # Raise an error if the stack is empty.

    def get(self):
        """
        Get the item from the top of the stack without removing it.

        Returns:
        - item: The item from the top of the stack.
        
        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():  # Check if the stack is not empty.
            return self.__items[-1]  # Return the last item from the list without removing it.
        else:
            raise IndexError("Getting from an empty stack")  # Raise an error if the stack is empty.

    def size(self):
        """
        Get the number of items in the stack.

        Returns:
        - int: The number of items in the stack.
        """
        return len(self.__items)  # Return the length of the list.

    def __str__(self) -> str:
        """
        Get a string representation of the stack.

        Returns:
        - str: A string representation of the stack.
        """
        return '\n'.join([(f'{i+1}. <{x}>') for i, x in enumerate(self.__items)])  # Join items with indexes for string representation.

    """
    OOP Principles applied

    Encapsulation:
    The Stack class encapsulates its internal state (items) and methods (is_empty, push, pop, get, size, __str__) within a single unit. 
    This prevents direct access to internal data and behavior from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    Programmers interact with the stack class using high-level methods like push, pop, get, etc., without needing to know the internal implementation details of these methods. They are abstracted away from the complexities of managing the stack's internal list structure, allowing for a simpler and more intuitive interface.

    Polymorphism:
    The push, pop, get, and size methods provide a common interface for interacting with the stack object. 
    This flexibility allows users to work with the stack using different methods depending on their specific needs, without needing to worry about the underlying implementation details.

    Modularity:
    Each method in the Stack class serves a specific purpose, promoting modularity and code reusability. 
    For example, the push method is responsible for adding items to the stack, 
    while the pop method is responsible for removing items from the stack. 
    This modular design makes the class easier to understand, maintain, and extend.
    """