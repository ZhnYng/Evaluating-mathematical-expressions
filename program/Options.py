# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# Class representing a set of options for manipulating assignment statements and equations.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : Options.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------

from ADT import DoubleStatement, Statement  # Import necessary data structures from ADT module
from utils import (
    ParseTree,
    EquationParseTree,
    FileHandler,
    MergeSort,
)  # Import utilities for parsing, file handling, and sorting

class Options:
    """
    Class representing a set of options for manipulating assignment statements and equations.
    """

    def __init__(self) -> None:
        """
        Initializes an Options object with an empty parse tree.
        """
        self.__parse_tree = ParseTree()  # Initialize a ParseTree object to store assignment statements
        self.__eqn_parse_tree = EquationParseTree()  # Initialize an EquationParseTree object

    def get_parse_tree(self):
        """
        Returns the parse tree object.
        """
        return self.__parse_tree

    def set_parse_tree(self, new_parse_tree: ParseTree):
        """
        Sets a new parse tree object.

        Parameters:
        new_parse_tree (ParseTree): The new parse tree object.
        """
        self.__parse_tree = new_parse_tree  # Set a new parse tree object

    def get_eqn_parse_tree(self):
        """
        Returns the equation parse tree object.
        """
        return self.__eqn_parse_tree

    def set_eqn_parse_tree(self, eqn_parse_tree: ParseTree):
        """
        Sets a new equation parse tree object.

        Parameters:
        eqn_parse_tree (ParseTree): The new equation parse tree object.
        """
        self.__eqn_parse_tree = eqn_parse_tree  # Set a new equation parse tree object

    def add_or_modify(self, statement: Statement):
        """
        Adds or modifies an assignment statement in the parse tree.

        Parameters:
            statement (Statement): The statement object to be added or modified.
        """
        statement = Statement(statement)  # Convert the input statement into a Statement object
        self.__parse_tree.add_statement(
            statement.get_var(), statement.get_tokens()
        )  # Add the statement to the parse tree

    def display_statements(self):
        """
        Displays the assignment statements and their evaluated answers.

        Returns:
            dict: A dictionary containing assignment statements as keys and their evaluated answers as values.
        """
        statement_and_answers = {}  # Initialize an empty dictionary to store statement-answer pairs

        # Iterate through the parse tree statements in inorder traversal
        for key, expression in self.__parse_tree.get_statements().getitem_inorder():
            # Create a formatted assignment statement
            statement = f"{key}={expression.shallow_tree()}"
            # Evaluate the assignment and store the result
            answer = self.__parse_tree.evaluate(key, expression)
            statement_and_answers[statement] = (
                answer  # Add the statement-answer pair to the dictionary
            )

        return statement_and_answers  # Return the dictionary containing statement-answer pairs

    def eval_one_var(self, var: str):
        """
        Evaluate and return the parse tree and result for a specific variable.

        Parameters:
            var (str): The variable for which to evaluate the parse tree.

        Returns:
            tuple: A tuple containing the parse tree string and the result of evaluating the variable.

        Raises:
            ValueError: If the expression for the variable does not exist in the parse tree.
        """
        expression = self.__parse_tree.get_statements()[
            var
        ]  # Get the expression corresponding to the variable

        if expression:
            # Generate the parse tree string
            expression_tree_str = expression.print_in_order(0)
            # Evaluate the variable using the parse tree
            result = self.__parse_tree.evaluate(var, expression)
            return (
                expression_tree_str,
                result,
            )  # Return the parse tree string and the result
        else:
            # Raise an error if the expression for the variable does not exist
            raise ValueError("Expression does not exist.")

    def read_from_file(self, file):
        """
        Reads assignment statements from a file and adds them to the parse tree.

        Parameters:
            file (str): The path to the input file.

        Returns:
            dict: A dictionary containing assignment statements as keys and their evaluated answers as values.
        """
        file_handler = FileHandler()  # Create a FileHandler object for reading the file
        statements = file_handler.read(
            file, read_mode="line"
        )  # Read assignment statements from the file
        for statement in statements:
            self.add_or_modify(
                statement
            )  # Add each statement to the parse tree

        return (
            self.display_statements()
        )  # Return the dictionary containing statement-answer pairs

    def sorting_expressions(self, output_file):
        """
        Sorts assignment statements by their evaluated values and writes them to an output file.

        Parameters:
            output_file (str): The path to the output file.

        Raises:
            ValueError: If there are no statements to sort.
        """
        if (
            str(self.display_statements()) == "{}"
        ):  # Check if there are any statements to sort
            raise ValueError("No statements to sort.")

        sorter = MergeSort(
            self.display_statements()
        )  # Create a MergeSort object for sorting
        sorter.merge_sort()  # Sort the assignment statements
        sorted_dict = (
            sorter.get_sorted_dict()
        )  # Get the sorted dictionary of statements

        sorted_output = ""  # Initialize an empty string to store sorted statements

        # Iterate through the sorted dictionary
        for answer, list_of_eqns in sorted_dict.items():
            formatted = ""
            if sorted_output:
                formatted += "\n"
            formatted += f"*** Statements with value=> {answer}\n"
            for eqn in list_of_eqns:
                formatted += f"{eqn}\n"
            sorted_output += (
                formatted  # Add the formatted statements to the sorted output
            )

        # Write to file
        file_handler = FileHandler()  # Create a FileHandler object for writing to file
        file_handler.write(
            output_file, sorted_output
        )  # Write the sorted statements to the output file

    def get_equation_tree(self, equation):
        """
        Get the parse tree of an equation.

        Parameters:
            equation (str): The equation string.

        Returns:
            EquationParseTreeNode: The parse tree of the equation.
        """
        # Convert the input equation string into a DoubleStatement object
        eqn = DoubleStatement(equation)
        # Add the equation to the equation parse tree and get its unique identifier
        id = self.__eqn_parse_tree.add_statement(eqn.get_tokens())
        # Retrieve the equation parse tree using its unique identifier
        equation_tree = self.__eqn_parse_tree.get_equations()[id]
        return equation_tree  # Return the parse tree of the equation

    def eval_equation(self, equation):
        """
        Evaluate an equation.

        Parameters:
            equation (str): The equation string.

        Returns:
            bool: True if the equation is equal, False otherwise.
        """
        # Get the parse tree of the equation using the get_equation_tree method
        equation_tree = self.get_equation_tree(equation)
        # Evaluate the equation parse tree and return the result
        return self.__eqn_parse_tree.evaluate_equation(
            equation_tree, self.__parse_tree.get_statements()
        )

    def make_subject_of_eqn(self, equation, target):
        """
        Rearrange an equation to make a specified variable the subject.

        Parameters:
            equation (str): The equation string.
            target (str): The variable to make the subject.

        Returns:
            str: The rearranged equation.
        """
        # Get the parse tree of the equation using the get_equation_tree method
        equation_tree = self.get_equation_tree(equation)
        # Rearrange the equation parse tree to make the target variable the subject
        rearranged_tree = self.__eqn_parse_tree.rearrange_tree(target, equation_tree)
        # Convert the rearranged equation parse tree back to bracket notation
        return rearranged_tree.bracket_inorder_traversal(string=True)