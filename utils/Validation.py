class Validation:
    def __init__(self):
        # Encapsulation of state using a private attribute with double underscores
        self.__valid_name = None

    def __check_empty(self, variable_name):
        # Abstraction: A private method abstracts the logic for checking if the variable name is empty.
        return bool(variable_name)

    def __check_starts_with_letter_or_underscore(self, variable_name):
        # Abstraction: A private method abstracts the logic for checking if the variable name starts with a letter or an underscore.
        if not variable_name:
            return False  # Handle empty strings
        first_char = variable_name[0]
        return first_char.isalpha() or first_char == '_'

    def __check_invalid_characters(self, variable_name):
        # Abstraction: A private method abstracts the logic for checking if the variable name contains only valid characters.
        return all(char.isalnum() or char == '_' for char in variable_name)

    def validate_variable_name(self, variable_name):
        validation_functions = [
            self.__check_empty,
            self.__check_starts_with_letter_or_underscore,
            self.__check_invalid_characters,
        ]

        error_messages = {
            self.__check_empty: "Variable name cannot be empty.",
            self.__check_starts_with_letter_or_underscore: "Variable name must start with a letter or underscore.",
            self.__check_invalid_characters: "Variable name contains invalid characters.",
        }

        for validation_function in validation_functions:
            if not validation_function(variable_name):
                error_message = error_messages[validation_function]
                raise ValueError(error_message)

        self.__valid_name = True
        return True
    
    def contains_spaces(self, statement):
        # Abstraction: A private method abstracts the logic for checking if the statement contains spaces.
        return ' ' in statement

    def is_valid(self):
        # Encapsulation: The state (__valid_name) is encapsulated, and this method provides controlled access to it.
        return self.__valid_name is True

    def is_invalid(self):
        # Encapsulation: The state (__valid_name) is encapsulated, and this method provides controlled access to it.
        return self.__valid_name is False
        
    def is_operator_and_operand_matching(self, tokens: list[str]):
        supported_operators = ['+', '-', '*', '/', '**']

        # Separate operators and variables/constants
        operators = [term for term in tokens if term in supported_operators]
        var_or_num = [term for term in tokens if term.isalnum() or term.replace(".", "").isnumeric()]

        # Check if there's at least one variable or constant
        if not var_or_num:
            raise ValueError('Expression must have at least one number or variable')

        # Check if the number of operators matches the number of variables/constants
        if len(operators) + 1 != len(var_or_num):
            raise ValueError(f'Number of valid operators does not match the number of variables in {" ".join(tokens)}.')

        return tokens

    def check_parentheses(self, tokens):
        opening = "([{"
        closing = ")]}"
        pairs = {')': '(', ']': '[', '}': '{'}
        """
        Check if the brackets in the input string are properly matched.

        Parameters:
            tokens (str): The input string to check.

        Returns:
            bool: True if brackets are properly matched, False otherwise.
        """
        stack = []
        operator_count = 0

        for char in tokens:
            if char in opening:
                stack.append(char)
            elif char in ['+', '-', '*', '/', '**']:
                operator_count += 1
                if len(stack) < operator_count:
                    return False
            elif char in closing:
                # If a closing bracket is encountered, check if the corresponding opening bracket is on the stack.
                if not stack or stack[-1] != pairs[char]:
                    return False
                operator_count = 0
                stack.pop()

        # If the stack is empty at the end, all brackets have been properly matched.
        is_fully_paren = not stack and any(char in opening or char in closing for char in tokens)
        return is_fully_paren