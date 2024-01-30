from AbstractClasses import Node
from utils import ExpressionTokenizer, Validation
import re

class Statement(Node):
    def __init__(self, statement):
        statement = statement.replace(" ", "")
        var, exp = self.split_statement(statement)

        tokenizer = ExpressionTokenizer()
        tokens = tokenizer.tokenize_expression(exp)

        # Validating operations of expression
        validation = Validation()
        validation.is_operator_and_operand_matching(tokens)

        # Expression must be fully parenthesized
        if not validation.check_parentheses(tokens):
            raise ValueError('Expressions must be fully parenthesized')
        
        super().__init__()
        self.__statement = statement
        self.__var = var
        self.__exp = exp
        self.tokens = tokens

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

    def split_statement(self, statement):
        try:
            var, exp = statement.split('=')
        except ValueError:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")
        
        if '=' not in statement or statement.count('=') != 1 or not var or not exp:
            raise ValueError(f"Invalid statement format in {statement}. It should be in the form 'var = exp'")

        return var, exp
        
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