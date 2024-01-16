from AbstractClasses import Node
from utils import BracketChecker
from exceptions import UnbalancedParenthesesError

class Statement(Node):
    def __init__(self, statement):
        statement = statement.replace(" ", "")
        var, exp = statement.split('=')
        bracket_checker = BracketChecker()
        is_fully_paren = bracket_checker.check(exp)
        if not is_fully_paren:
            raise UnbalancedParenthesesError("Statement is not fully parenthesized")

        super().__init__()
        self.__statement = statement
        self.__var = var
        self.__exp = exp

    @property
    def statement(self):
        """Returns the statement."""
        return self.__statement
    
    @property
    def var(self):
        """Returns the statement."""
        return self.__var
    @property
    def exp(self):
        """Returns the statement."""
        return self.__exp

    @statement.setter
    def statement(self, statement):
        """Sets the statement."""
        self.__statement = statement

    @var.setter
    def var(self, var):
        """Sets the statement."""
        self.__statement = var

    @exp.setter
    def exp(self, exp):
        """Sets the statement."""
        self.__statement = exp

    def __lt__(self, other):
        """
        Less than comparison for Files.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var < other.__var
    
    def __str__(self):
        return f"{self.__statement}"