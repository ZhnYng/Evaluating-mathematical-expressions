class Validation:
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