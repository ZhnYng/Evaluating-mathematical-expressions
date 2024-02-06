# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Initializes an ExpressionTokenizer object with an empty list 
# of tokens and a set of valid special characters.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : ExpressionTokenizer.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
class ExpressionTokenizer:
    def __init__(self):
        """
        Initializes an ExpressionTokenizer object with an empty list of tokens and a set of valid special characters.
        """
        self.valid_special_chars = {'+', '-', '*', '/', '**', '(', ')'}  # Set of valid special characters
        self.__tokens = []  # List to store tokens extracted from the expression

    def get_tokens(self):
        """
        Gets the list of tokens.

        Returns:
        list: The list of tokens.
        """
        return self.__tokens
    
    def set_tokens(self, tokens):
        """
        Sets the list of tokens.

        Parameters:
        tokens (list): The list of tokens to set.
        """
        self.__tokens = tokens

    def __is_valid_special_char(self, char):
        """
        Checks if a character is a valid special character.

        Parameters:
        char (str): The character to check.

        Returns:
        bool: True if the character is a valid special character, False otherwise.
        """
        return char in self.valid_special_chars

    def tokenize_expression(self, expression):
        """
        Tokenizes an arithmetic expression.

        Parameters:
        expression (str): The arithmetic expression to tokenize.

        Returns:
        list: A list of tokens extracted from the expression.
        """
        current_token = ''  # Current token being constructed
        last_token = None  # Last token encountered
        paren_depth = 0  # Depth of nested parentheses
        token_count_since_last_paren = 0  # Count of tokens since last '('

        for i, char in enumerate(expression):
            if char.isspace():  # Skip whitespace characters
                continue

            if char.isalnum() or char == '.':  # Alphanumeric characters and '.' are part of tokens
                current_token += char
                last_token = char
                
            elif self.__is_valid_special_char(char):  # Valid special characters
                if current_token:
                    self.__tokens.append(current_token)  # Add current token to the list
                    current_token = ''  # Reset current token
                    if paren_depth > 0:
                        token_count_since_last_paren += 1

                # Handling single negative values e.g. (-3) get converted to (0-3)
                if char == '-' and last_token == '(':
                    if self.allow_exp_alter():  # Prompt user for expression alteration
                        self.__tokens.append('0')  # Add '0' to represent subtraction
                        token_count_since_last_paren += 1
                    else:
                        raise PermissionError("Expression alteration denied")

                if char == '(':  # Opening parenthesis
                    paren_depth += 1
                    token_count_since_last_paren = 0
                elif char == ')' and paren_depth > 0:  # Closing parenthesis
                    paren_depth -= 1
                    # Handling single positive values e.g. (3) get converted to (3+0)
                    if token_count_since_last_paren == 1:  # Only one token since last '('
                        if self.allow_exp_alter():  # Prompt user for expression alteration
                            self.__tokens.extend(['+', '0'])  # Add '+' and '0' for addition
                            token_count_since_last_paren += 1
                        else:
                            raise PermissionError("Expression alteration denied")

                if char == '*' and last_token == '*':  # Handle power operation
                    self.__tokens[-1] = '**'
                else:
                    self.__tokens.append(char)  # Add valid special character to the list
                last_token = char  # Update last token
            else:
                raise ValueError(f"Invalid character: {char}")  # Raise error for invalid character

        if current_token:
            self.__tokens.append(current_token)  # Add any remaining token to the list

        return self.__tokens  # Return the list of tokens
    
    def allow_exp_alter(self):
        """
        Prompts the user for permission to alter the expression format.

        Returns:
        bool: True if the user agrees to alter the expression, False otherwise.
        """
        allow_alter = input('\nExpressions must follow operand, operator, operand format.\
                            \nBy proceeding you agree to altering the expression to this format.\
                            \nProceed?(Y/N): ').upper()
        if allow_alter == "Y":
            return True
        return False

    """
    OOP Principles Applied:

    Encapsulation:
    The ExpressionTokenizer class encapsulates the functionality related to tokenizing arithmetic expressions within a single unit.
    Internal data, such as the list of tokens and the set of valid special characters, are encapsulated within the class, promoting data integrity and reducing complexity.
    External classes interact with ExpressionTokenizer through defined methods, maintaining encapsulation boundaries.

    Abstraction:
    ExpressionTokenizer abstracts away the complexities of tokenizing arithmetic expressions by providing a high-level tokenize_expression method.
    Users interact with ExpressionTokenizer without needing to know the internal implementation details of tokenization, promoting a simpler and more intuitive interface.

    Polymorphism:
    The ExpressionTokenizer class can tokenize different arithmetic expressions seamlessly.
    The tokenize_expression method can handle various scenarios, such as handling negative and positive values, and power operations, without changes to its interface.

    Modularity:
    The tokenize_expression method serves a specific purpose of tokenizing arithmetic expressions, promoting modularity and code reusability.
    This modular design makes the ExpressionTokenizer class easier to understand, maintain, and extend.
    """