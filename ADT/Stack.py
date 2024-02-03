class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.__items = []

    @property
    def items(self):
        """
        Get the items in the stack.
        """
        return self.__items

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        - item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
        - item: The item from the top of the stack.
        
        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Popping from an empty stack")

    def get(self):
        """
        Get the item from the top of the stack without removing it.

        Returns:
        - item: The item from the top of the stack.
        
        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Getting from an empty stack")

    def size(self):
        """
        Get the number of items in the stack.

        Returns:
        - int: The number of items in the stack.
        """
        return len(self.items)
    
    def __str__(self) -> str:
        """
        Get a string representation of the stack.

        Returns:
        - str: A string representation of the stack.
        """
        return '\n'.join([(f'{i+1}. <{x}>') for i, x in enumerate(self.items)])