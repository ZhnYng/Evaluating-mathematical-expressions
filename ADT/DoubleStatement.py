#-----------------------------------------------------
# ST1507 DSAA 
# CA2
#
# Represents a double statement, consisting of two equations separated by an equals sign.
# Attributes:
#     __equation (str): The original equation string.
#     __double_tokens (list): The tokens of the complete double statement.
#
#-----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : DoubleStatement.py
#
#-----------------------------------------------------
# To run: python main.py
#-----------------------------------------------------

from utils.ExpressionTokenizer import ExpressionTokenizer
from utils.Validation import Validation
from ADT import Statement

class DoubleStatement(Statement):
    """
    Represents a double statement, consisting of two equations separated by an equals sign.

    Attributes:
        __equation (str): The original equation string.
        __double_tokens (list): The tokens of the complete double statement.
    """

    def __init__(self, equation):
        """
        Initializes a DoubleStatement object with the given equation.

        Parameters:
            equation (str): The equation string containing two expressions separated by an equals sign.
        """
        self.validation = Validation()

        # Split the equation into two expressions
        exp1, exp2 = self.split_statement(equation)

        # Tokenize the expressions
        tokenizer = ExpressionTokenizer()
        tokens1 = tokenizer.tokenize_expression(exp1)

        # Reinitialize tokenizer because it saves the tokens as an attribute
        tokenizer = ExpressionTokenizer()
        tokens2 = tokenizer.tokenize_expression(exp2)

        # Validate both expressions
        self.validation.validate_expression(tokens1)  # Use expression validation
        self.validation.validate_expression(tokens2)  

        # Update the equation tokens to include both parts
        self.__equation = equation
        self.__double_tokens = tokens1 + ['='] + tokens2

    def get_equation(self):
        """Returns the original equation string."""
        return self.__equation

    def set_equation(self, equation):
        """
        Sets the original equation string.

        Parameters:
            equation (str): The new equation string.
        """
        self.__equation = equation

    def get_tokens(self):
        """Returns the complete tokens for the equation."""
        return self.__double_tokens
    
    def set_tokens(self, double_tokens):
        """
        Sets the complete tokens for the equation.

        Parameters:
            double_tokens (list): The new list of tokens for the equation.
        """
        self.__double_tokens = double_tokens

    def __str__(self):
        """Get a string representation of the DoubleStatement."""
        return f"{self.__equation}"
    
    """
    OOP Principles applied:

    Encapsulation:
    The DoubleStatement class encapsulates the attributes __equation and __double_tokens, as well as the 
    validation instance within a single unit. This prevents direct access to internal data and behavior 
    from outside the class, promoting data integrity and reducing complexity.

    Abstraction:
    The use of the ExpressionTokenizer and Validation classes abstracts away the complexities of tokenizing 
    expressions and validating them. Users interact with the DoubleStatement class using high-level methods 
    without needing to know the internal implementation details.

    Modularity:
    Each method in the DoubleStatement class serves a specific purpose, promoting modularity and code reusability. 
    The class follows the principle of single responsibility, where each method is responsible for a single task.

    Inheritance:
    The DoubleStatement class inherits from the Statement class, demonstrating inheritance, which allows 
    the DoubleStatement class to inherit behavior and attributes from its parent class.
    """