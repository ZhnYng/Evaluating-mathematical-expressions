from AbstractClasses import Node
from utils import BracketChecker
from exceptions import UnbalancedParenthesesError
import Statement

class Equation(Node):
    def __init__(self, statement:Statement, answer):
        super().__init__()
        self.__statement = statement
        self.__answer = answer

    @property
    def statement(self):
        """Returns the statement."""
        return self.__statement
    
    @property
    def answer(self):
        """Returns the statement."""
        return self.__answer
    
    @statement.setter
    def statement(self, statement):
        """Sets the statement."""
        self.__statement = statement

    @answer.setter
    def answer(self, answer):
        """Sets the statement."""
        self.__answer = answer

    def __lt__(self, other):
        """
        Less than comparison for Equations.
        """
        if not isinstance(other, Equation):
            raise TypeError("Comparison not supported between instances of 'Equation' and other types")
        elif self.__answer < other.__answer:
            return True
        else:
            return self.__statement < other.__statement

    def __gt__(self, other):
        """
        Less than comparison for Equations.
        """
        if not isinstance(other, Equation):
            raise TypeError("Comparison not supported between instances of 'Equation' and other types")
        elif self.__answer > other.__answer:
            return True
        else:
            return self.__statement < other.__statement

    def __str__(self):
        return f"{self.__statement}={self.__answer}"