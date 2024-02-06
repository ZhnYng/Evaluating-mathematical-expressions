from utils.ExpressionTokenizer import ExpressionTokenizer
from utils.Validation import Validation
from ADT import Statement

class DoubleStatement(Statement):
    def __init__(self, equation):
        self.validation = Validation()
        exp1, exp2 = self.split_statement(equation)

        # Tokenize the expressions
        tokenizer = ExpressionTokenizer()
        tokens1 = tokenizer.tokenize_expression(exp1)

        tokenizer = ExpressionTokenizer()
        tokens2 = tokenizer.tokenize_expression(exp2)

        self.validation.validate_expression(tokens1)  # Reuse validation from Statement
        self.validation.validate_expression(tokens2)  # Reuse validation from Statement

        # Update the equation tokens to include both parts
        self.__equation = equation
        self.__double_tokens = tokens1 + ['='] + tokens2

    def get_tokens(self):
        """Returns the complete tokens for the equation."""
        return self.__double_tokens

    def __str__(self):
        """Get a string representation of the DoubleStatement."""
        return f"{self.__equation}"