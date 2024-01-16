class BracketChecker:
    """
    A class for checking if brackets in a given string are properly matched.
    """
    def __init__(self):
        """
        Initialize the BracketChecker class with opening brackets, closing brackets,
        and bracket pairs.
        """
        self.opening = "([{"
        self.closing = ")]"
        self.pairs = {')': '(', ']': '[', '}': '{'}

    def check(self, input_str):
        """
        Check if the brackets in the input string are properly matched.

        Parameters:
            input_str (str): The input string to check.

        Returns:
            bool: True if brackets are properly matched, False otherwise.
        """
        stack = []

        for char in input_str:
            if char in self.opening:
                stack.append(char)
            elif char in self.closing:
                # If a closing bracket is encountered, check if the corresponding opening bracket is on the stack.
                if not stack or stack[-1] != self.pairs[char]:
                    return False
                stack.pop()

        # If the stack is empty at the end, all brackets have been properly matched.
        return not stack