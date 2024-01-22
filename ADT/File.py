from AbstractClasses import Node

class File(Node):
    def __init__(self, name, key=None):
        """
        Initializes a File node with a given name and an optional key.
        """
        super().__init__()
        if not name.lower().endswith(('.txt')):
            raise ValueError('File type invalid!')
        self.__name = name
        self.key = key

    @property
    def name(self):
        """Returns the name of the File."""
        return self.__name

    @name.setter
    def name(self, value):
        """Sets the name of the File."""
        self.__init__(value)

    def __eq__(self, other):
        """
        Checks equality based on the name and key of the File.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return (self.name, self.key) == (other.name, other.key)

    def __lt__(self, other):
        """
        Less than comparison for Files.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return (self.key, self.name) < (other.key, other.name)

    def __le__(self, other):
        """
        Less than or equal to comparison for Files.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return (self.name, self.key) == (other.name, other.key) or (self.key, self.name) < (other.key, other.name)

    def __gt__(self, other):
        """
        Greater than comparison for Files.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return not (self.name, self.key) == (other.name, other.key) or (self.key, self.name) < (other.key, other.name)

    def __ge__(self, other):
        """
        Greater than or equal to comparison for Files.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return not (self.key, self.name) < (other.key, other.name)

    def __str__(self):
        """Returns the File's name as its string representation."""
        return self.name
