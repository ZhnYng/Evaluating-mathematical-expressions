class SortedList:
    """
    Class representing a sorted linked list.
    """
    def __init__(self):
        """
        Initializes a new SortedList with 'headNode' set to None (empty list)
        and 'length' set to 0 to track the number of nodes in the list.
        """
        self.headNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        """
        Private helper method to append a new node at the head of the list.
        """
        newNode.nextNode = self.headNode  # Link new node to the current head
        self.headNode = newNode  # Update the head to be the new node
        self.length += 1  # Increment the length of the list

    def insert(self, newNode):
        """
        Inserts a new node into the sorted list in the correct position.
        """
        # Handling the case where the list is empty
        if self.headNode is None:
            self.headNode = newNode
            self.length += 1
            return

        # Handling the case where the new node should be the new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Iterating through the list to find the correct position for the new node
        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode is not None:
            if newNode < rightNode:
                newNode.nextNode = rightNode
                leftNode.nextNode = newNode
                self.length += 1
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        # If the correct position is at the end of the list
        leftNode.nextNode = newNode
        self.length += 1

    def items(self):
        nodes = [node.__str__() for node in self.iterate()]  # List comprehension to convert each node to string
        return nodes

    def __str__(self):
        """
        Optimized __str__ method using .join instead of +=

        Returns a string representation of the sorted list.
        """
        nodes = [str(f"'{node}'") for node in self.iterate()]  # List comprehension to convert each node to string
        return ','.join(nodes)  # Joining all node strings with a comma

    def iterate(self):
        """
        Generator to iterate over each node in the list.
        """
        current = self.headNode
        while current is not None:
            yield current  # Yielding each node one by one
            current = current.nextNode