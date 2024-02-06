from ADT import DoubleStatement, Statement  # Import necessary data structures from ADT module
from utils import (
    ParseTree,
    EquationParseTree,
    FileHandler,
    MergeSort,
)  # Import utilities for parsing, file handling, and sorting
import re

class Options:
    def __init__(self) -> None:
        """
        Initializes an Options object with an empty parse tree.
        """
        self.__parse_tree = (
            ParseTree()
        )  # Initialize a ParseTree object to store assignment statements
        self.__eqn_parse_tree = EquationParseTree()

    # Getter function
    def get_parse_tree(self):
        """
        Returns the parse tree object.
        """
        return self.__parse_tree

    # Setter function
    def set_parse_tree(self, new_parse_tree: ParseTree):
        """
        Sets a new parse tree object.

        Parameters:
        new_parse_tree (ParseTree): The new parse tree object.
        """
        self.__parse_tree = new_parse_tree  # Set a new parse tree object

    # Getter function
    def get_eqn_parse_tree(self):
        """
        Returns the parse tree object.
        """
        return self.__eqn_parse_tree

    # Setter function
    def set_eqn_parse_tree(self, eqn_parse_tree: ParseTree):
        """
        Sets a new parse tree object.

        Parameters:
        new_parse_tree (ParseTree): The new parse tree object.
        """
        self.__eqn_parse_tree = eqn_parse_tree  # Set a new parse tree object

    def add_or_modify(self, statement: Statement):
        """
        Adds or modifies an assignment statement in the parse tree.

        Parameters:
            statement (Statement): The statement object to be added or modified.
        """
        statement = Statement(
            statement
        )  # Convert the input statement into a Statement object
        # Record new statement
        self.__parse_tree.add_statement(
            statement.get_var(), statement.get_tokens()
        )  # Add the statement to the parse tree

    def display_statements(self):
        """
        Displays the assignment statements and their evaluated answers.

        Returns:
            dict: A dictionary containing assignment statements as keys and their evaluated answers as values.
        """
        statement_and_answers = (
            {}
        )  # Initialize an empty dictionary to store statement-answer pairs

        # Iterate through the parse tree statements in inorder traversal
        for key, expression in self.__parse_tree.get_statements().getitem_inorder():
            # Create a formatted assignment statement
            statement = f"{key}={expression.return_tree()}"
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
            expression_tree_str = expression.printInOrder(0)
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
            self.add_or_modify(statement)  # Add each statement to the parse tree

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
        eqn = DoubleStatement(equation)  # Convert the input statement into a Equation object
        id = self.__eqn_parse_tree.add_statement(
            eqn.get_tokens()
        )  # Add the equation to the parse tree
        equation_tree = self.__eqn_parse_tree.get_equations()[id]  # get the equation parse tree using the id
        return equation_tree

    def eval_equation(self, equation):
        equation_tree = self.get_equation_tree(equation)
        return self.__eqn_parse_tree.evaluate_equation(
            equation_tree, self.__parse_tree.get_statements()
        )  # evaluate the equation

    def make_subject_of_eqn(self, equation, target):
        rearranged_tree = self.__eqn_parse_tree.rearrange_tree(
            target, self.get_equation_tree(equation)
        )  # Rearrange parse tree to keep target variable on the left
        return rearranged_tree.bracket_inorder_traversal(
            string=True
        )  # Convert back to bracket notation

    """
    OOP Principles Applied:

    Encapsulation:
    - The Options class encapsulates the functionality related to managing assignment statements and their evaluation within a single unit.
    - Internal data and behavior, such as the parse tree, are encapsulated within the class, promoting data integrity and reducing complexity.
    - External classes interact with Options through defined methods, maintaining encapsulation boundaries.

    Abstraction:
    - Options class abstracts away the complexities of managing assignment statements and their evaluation by providing high-level methods like add_or_modify, display_statements, eval_one_var, read_from_file, and sorting_expressions.
    - Users interact with Options without needing to know the internal implementation details of these methods, promoting a simpler and more intuitive interface.

    Polymorphism:
    - The Options class can handle different types of input, such as individual assignment statements or statements read from a file, seamlessly.
    - Methods like add_or_modify, eval_one_var, read_from_file, and sorting_expressions are flexible and can accommodate various scenarios without changes to their interface.

    Modularity:
    - Each method in the Options class serves a specific purpose, promoting modularity and code reusability.
    - For example, the add_or_modify method is responsible for adding or modifying assignment statements in the parse tree, while the sorting_expressions method is responsible for sorting expressions and writing them to an output file.
    - This modular design makes the Options class easier to understand, maintain, and extend.
    """