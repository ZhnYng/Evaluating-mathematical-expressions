from AbstractClasses import Node
from utils import BracketChecker
import re

class Statement(Node):
    def __init__(self, statement):
        statement = statement.replace(" ", "")
        var, exp = statement.split('=')

        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError("Invalid statement format. It should be in the form 'var = exp'")

        # Validating value of expression
        supported_operators = ['+', '-', '*', '/', '**']
        supported = any(operator in exp for operator in supported_operators)
        if not supported:
            def strip_all_brackets(expression):
                while '(' in expression:
                    start = expression.rfind('(')
                    end = expression.find(')', start)
                    if start != -1 and end != -1:
                        expression = expression[:start] + expression[start+1:end] + expression[end+1:]
                return expression

            temp_exp = strip_all_brackets(exp)
            if not temp_exp.isnumeric() or not temp_exp.replace(".", "").isnumeric():
                raise ValueError(f"Invalid expression format. Only {supported_operators} are accepted.")
            else:
                exp = f'({temp_exp}+0)' # Keep format of expressions consistent

        # Expression must be fully parenthesized
        bracket_checker = BracketChecker()
        is_fully_paren = bracket_checker.check(exp)
        if not is_fully_paren:
            raise ValueError('Expressions must be fully parenthesized')

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

    def __gt__(self, other):
        """
        Greater than comparison for Files.
        """
        if not isinstance(other, Statement):
            raise TypeError("Comparison not supported between instances of 'Statement' and other types")
        return self.__var > other.__var
    
    def __str__(self):
        return f"{self.__statement}"