# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Initialize the Validation object with an attribute to store the validation status.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : Validation.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
class Validation:
    def __init__(self):
        """
        Initialize the Validation object with an attribute to store the validation status.
        """
        # Encapsulation of state using a private attribute with double underscores
        self.__valid_name = None

    def get_valid_name(self):
        return self.__valid_name
    
    def set_valid_name(self, valid_name):
        self.__valid_name = valid_name

    def __check_empty(self, variable_name):
        """
        Check if the variable name is empty.

        Parameters:
            variable_name (str): The variable name to be checked.

        Returns:
            bool: True if the variable name is not empty, False otherwise.
        """
        # Abstraction: A private method abstracts the logic for checking if the variable name is empty.
        return bool(variable_name)

    def __check_only_contains_letters(self, variable_name):
        """
        Check if the variable name only contains letter.

        Parameters:
            variable_name (str): The variable name to be checked.

        Returns:
            bool: True if the variable name contains only letters, False otherwise.
        """
        # Abstraction: A private method abstracts the logic for checking if the variable name contains only letters.
        if not variable_name:
            return False  # Handle empty strings
        return all(char.isalpha() for char in variable_name)

    def validate_variable_name(self, variable_name):
        """
        Validate the format of a variable name.

        Parameters:
            variable_name (str): The variable name to be validated.

        Returns:
            bool: True if the variable name is valid, False otherwise.

        Raises:
            ValueError: If the variable name does not meet the validation criteria.
        """
        # List of validation functions to be applied
        validation_functions = [
            self.__check_empty,
            self.__check_only_contains_letters
        ]

        # Error messages corresponding to each validation function
        error_messages = {
            self.__check_empty: "Variable name cannot be empty.",
            self.__check_only_contains_letters: "Variable name must only contain letters.",
        }

        # Iterate over each validation function
        for validation_function in validation_functions:
            # Apply the validation function to the variable name
            if not validation_function(variable_name):
                # If validation fails, retrieve the corresponding error message
                error_message = error_messages[validation_function]
                # Raise a ValueError with the error message
                raise ValueError(error_message)

        # If all validations pass, set the __valid_name attribute to True and return True
        self.__valid_name = True
        return True

    def contains_spaces(self, statement):
        """
        Check if the statement contains spaces.

        Parameters:
            statement (str): The statement to be checked.

        Returns:
            bool: True if the statement contains spaces, False otherwise.
        """
        # Abstraction: A private method abstracts the logic for checking if the statement contains spaces.
        return ' ' in statement

    def is_valid(self):
        """
        Check if the validation is successful.

        Returns:
            bool: True if the validation is successful, False otherwise.
        """
        # Encapsulation: The state (__valid_name) is encapsulated, and this method provides controlled access to it.
        return self.__valid_name is True

    def is_invalid(self):
        """
        Check if the validation is unsuccessful.

        Returns:
            bool: True if the validation is unsuccessful, False otherwise.
        """
        # Encapsulation: The state (__valid_name) is encapsulated, and this method provides controlled access to it.
        return self.__valid_name is False
    
    def __is_dividing_by_zero(self, tokens: list[str]):
        """
        Check if the expression contains division by zero.

        Parameters:
            tokens (list of str): The tokens of the expression.

        Raises:
            ZeroDivisionError: If division by zero is detected.
        """
        # Convert the list to a string
        list_as_string = ''.join(tokens)

        # Search for the pattern
        if '/0' in list_as_string:
            raise ZeroDivisionError('Expression cannot be divided by 0')
        
    def __is_operator_and_operand_matching(self, tokens: list[str]):
        """
        Validate if operator and operand is matching in the expression.

        Parameters:
            tokens (list of str): The tokens of the expression.

        Returns:
            list of str: The tokens of the expression.

        Raises:
            ValueError: If the number of operators does not match the number of operands.
        """
        # Validate if operator and operand is matching e.g. (3+1) is valid and (1++) is invalid.
        supported_operators = ['+', '-', '*', '/', '**']

        # Separate operators and variables/constants
        operators = [term for term in tokens if term in supported_operators]
        var_or_num = [term for term in tokens if term.isalnum() or term.replace(".", "").isnumeric()]

        # Check if there's at least one variable or constant
        if not var_or_num:
            raise ValueError('Expression must have at least one number or variable')

        # Check if the number of operators matches the number of variables/constants
        if len(operators) + 1 != len(var_or_num):
            raise ValueError(f'Number of valid operators does not match the number of variables in {"".join(tokens)}.')

        return tokens

    def __check_parentheses(self, tokens):
        """
        Check if the parentheses in the input string are properly matched.

        Parameters:
            tokens (str): The input string to check.

        Raises:
            ValueError: If parentheses are not properly matched.
        """
        opening = "([{"
        closing = ")]}"
        pairs = {')': '(', ']': '[', '}': '{'}

        stack = []  # Stack to keep track of opening parentheses
        operator_count = 0  # Count of operators encountered

        for char in tokens:
            if char in opening:
                stack.append(char)  # Push opening parentheses onto the stack
            elif char in ['+', '-', '*', '/', '**']:
                operator_count += 1
                # Check if there are enough opening parentheses for the operators
                if len(stack) < operator_count:
                    raise ValueError('Expressions must be fully parenthesized')
            elif char in closing:
                # If a closing bracket is encountered, check if the corresponding opening bracket is on the stack.
                if not stack or stack[-1] != pairs[char]:
                    raise ValueError('Expressions must be fully parenthesized')
                
                operator_count -= 1  # Brackets for this operator has been checked
                if operator_count < 0:
                    raise ValueError('Unnecessary brackets found')
                
                stack.pop()  # Remove the corresponding opening bracket from the stack

        # If the stack is empty at the end, all brackets have been properly matched.
        is_fully_paren = not stack and any(char in opening or char in closing for char in tokens)
        if not is_fully_paren:
            raise ValueError('Expressions must be fully parenthesized')

    def validate_expression(self, expression):
        """
        Validate the expression format.

        Parameters:
            expression (str): The expression to be validated.

        Returns:
            bool: True if the expression is valid

        Raises:
            ValueError: If the expression format is not valid.
            ZeroDivisionError: If the expression cannot be divided by 0
        """
        validation_functions = [
            self.__is_dividing_by_zero,
            self.__is_operator_and_operand_matching,
            self.__check_parentheses,
        ]

        # Iterate through each validation function and call it with the expression
        for validation_function in validation_functions:
            validation_function(expression)

        return True