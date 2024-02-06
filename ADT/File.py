#-----------------------------------------------------
# ST1507 DSAA 
# CA2
#
# Represents a file node.
# Attributes:
#     name (str): The name of the file.
#
#-----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : File.py
#
#-----------------------------------------------------
# To run: python main.py
#-----------------------------------------------------

from AbstractClasses import Node

class File(Node):
    """
    Represents a file node.

    Attributes:
        name (str): The name of the file.
    """

    def __init__(self, name):
        """
        Initializes a File node with a given name.

        Parameters:
            name (str): The name of the file.
        
        Raises:
            ValueError: If the file type is invalid (not ending with '.txt').
        """
        super().__init__()
        if not name.lower().endswith('.txt'):
            raise ValueError('File type invalid!')
        self.__name = name

    @property
    def name(self):
        """
        Gets the name of the File.

        Returns:
            str: The name of the File.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Sets the name of the File.

        Parameters:
            value (str): The new name for the File.
        """
        self.__init__(value)

    def __eq__(self, other):
        """
        Checks equality based on the name of the File.

        Parameters:
            other (File): The other File object to compare.

        Returns:
            bool: True if the Files are equal, False otherwise.

        Raises:
            TypeError: If comparison is attempted with a non-File object.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return self.name == other.name

    def __lt__(self, other):
        """
        Less than comparison for Files.

        Parameters:
            other (File): The other File object to compare.

        Returns:
            bool: True if self is less than other, False otherwise.

        Raises:
            TypeError: If comparison is attempted with a non-File object.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return self.name < other.name

    def __le__(self, other):
        """
        Less than or equal to comparison for Files.

        Parameters:
            other (File): The other File object to compare.

        Returns:
            bool: True if self is less than or equal to other, False otherwise.

        Raises:
            TypeError: If comparison is attempted with a non-File object.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return self.name <= other.name

    def __gt__(self, other):
        """
        Greater than comparison for Files.

        Parameters:
            other (File): The other File object to compare.

        Returns:
            bool: True if self is greater than other, False otherwise.

        Raises:
            TypeError: If comparison is attempted with a non-File object.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return self.name > other.name

    def __ge__(self, other):
        """
        Greater than or equal to comparison for Files.

        Parameters:
            other (File): The other File object to compare.

        Returns:
            bool: True if self is greater than or equal to other, False otherwise.

        Raises:
            TypeError: If comparison is attempted with a non-File object.
        """
        if not isinstance(other, File):
            raise TypeError("Comparison not supported between instances of 'File' and other types")
        return self.name >= other.name

    def __str__(self):
        """
        Returns the File's name as its string representation.

        Returns:
            str: The name of the File.
        """
        return self.name

    """
    OOP Principles applied

    Encapsulation:
    The File class encapsulates the name attribute and methods within a single unit. 
    This promotes data integrity and reduces complexity.

    Abstraction:
    Programmers interact with the File class using high-level methods like __eq__, __lt__, __le__, __gt__, __ge__, __str__, etc., 
    without needing to know the internal implementation details. 
    This allows for a simpler and more intuitive interface.

    Polymorphism:
    The __eq__, __lt__, __le__, __gt__, and __ge__ methods handle comparison operations with other File objects seamlessly, 
    without needing to worry about the underlying implementation details. Even though they are individually separate comparison
    methods, polymorphism is still at play here, albeit in a slightly different way. Polymorphism allows these methods 
    to be invoked on File objects and have different behaviors.

    Modularity:
    Each method in the File class serves a specific purpose, promoting modularity and code reusability. 
    This modular design makes the class easier to understand, maintain, and extend.
    """