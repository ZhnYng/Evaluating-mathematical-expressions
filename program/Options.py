from ADT import Hashtable, Statement, SortedList  # Import necessary data structures from ADT module
from utils import ParseTree, FileHandler, MergeSort  # Import utilities for parsing, file handling, and sorting

# Import the necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

class Options:
    def __init__(self) -> None:
        """
        Initializes an Options object with an empty parse tree.
        """
        self.__parse_tree = ParseTree()  # Initialize a ParseTree object to store assignment statements
        self.historyLog = [] # Initialize an empty list to store all the user's history logs


    # Getter function
    def get_parse_tree(self):
        """
        Returns the parse tree object.
        """
        return self.__parse_tree

    # Setter function
    def set_parse_tree(self, new_parse_tree:ParseTree):
        """
        Sets a new parse tree object.

        Parameters:
        new_parse_tree (ParseTree): The new parse tree object.
        """
        self.__parse_tree = new_parse_tree  # Set a new parse tree object

    def add_or_modify(self, statement:Statement):
        """
        Adds or modifies an assignment statement in the parse tree.

        Parameters:
            statement (Statement): The statement object to be added or modified.
        """
        statement = Statement(statement)  # Convert the input statement into a Statement object
        # Record new statement
        self.__parse_tree.add_statement(statement.get_var(), statement.get_tokens())  # Add the statement to the parse tree
        # Log the history entry
        self.historyLog.append(("Add/Modify Assignment Statements - Input:", statement))

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
            statement = f"{key}={expression.return_tree()}"
            # Evaluate the assignment and store the result
            answer = self.__parse_tree.evaluate(key, expression)
            statement_and_answers[statement] = answer  # Add the statement-answer pair to the dictionary

        # Log the history entry
        self.historyLog.append(("Displayed Current Statements - Output:", statement_and_answers))
        
        return statement_and_answers  # Return the dictionary containing statement-answer pairs

    def eval_one_var(self, var:str):
        """
        Evaluate and return the parse tree and result for a specific variable.

        Parameters:
            var (str): The variable for which to evaluate the parse tree.

        Returns:
            tuple: A tuple containing the parse tree string and the result of evaluating the variable.
        
        Raises:
            ValueError: If the expression for the variable does not exist in the parse tree.
        """
        expression = self.__parse_tree.get_statements()[var]  # Get the expression corresponding to the variable

        if expression:
            # Generate the parse tree string
            expression_tree_str = expression.printInOrder(0)
            # Evaluate the variable using the parse tree
            result = self.__parse_tree.evaluate(var, expression)
            # Log the history entry
            self.historyLog.append(("Evaluated a single variable -\n", expression_tree_str))
            return expression_tree_str, result  # Return the parse tree string and the result
        else:
            # Raise an error if the expression for the variable does not exist
            raise ValueError('Expression does not exist.')
    
    
    def read_from_file(self, file):
        """
        Reads assignment statements from a file and adds them to the parse tree.

        Parameters:
            file (str): The path to the input file.

        Returns:
            dict: A dictionary containing assignment statements as keys and their evaluated answers as values.
        """
        file_handler = FileHandler()  # Create a FileHandler object for reading the file
        statements = file_handler.read(file, read_mode='line')  # Read assignment statements from the file
        for statement in statements:
            self.add_or_modify(statement)  # Add each statement to the parse tree
            
        # Log the history entry
        self.historyLog.append(("Read and Sort Assignment Statements from File - Input file:", file))

        return self.display_statements()  # Return the dictionary containing statement-answer pairs

    def sorting_expressions(self, output_file):
        """
        Sorts assignment statements by their evaluated values and writes them to an output file.

        Parameters:
            output_file (str): The path to the output file.

        Raises:
            ValueError: If there are no statements to sort.
        """
        if str(self.display_statements()) == '{}':  # Check if there are any statements to sort
            raise ValueError('No statements to sort.')
            
        sorter = MergeSort(self.display_statements())  # Create a MergeSort object for sorting
        sorter.merge_sort()  # Sort the assignment statements
        sorted_dict = sorter.get_sorted_dict()  # Get the sorted dictionary of statements

        sorted_output = ''  # Initialize an empty string to store sorted statements

        # Iterate through the sorted dictionary
        for answer, list_of_eqns in sorted_dict.items():
            formatted = ''
            if sorted_output:
                formatted += '\n'
            formatted += f'*** Statements with value=> {answer}\n'
            for eqn in list_of_eqns:
                formatted += f'{eqn}\n'
            sorted_output += formatted  # Add the formatted statements to the sorted output

        # Write to file
        file_handler = FileHandler()  # Create a FileHandler object for writing to file
        file_handler.write(output_file, sorted_output)  # Write the sorted statements to the output file
        # Log the history entry
        self.historyLog.append(("Sorted Expressions - Output File:", output_file))
        
    def displayHistory(self):
        print("\n--- Your history: ---\n")
        
        if not self.historyLog:
            print("No history log available.")
        else:
            # Iterate through each entry in the analysis history
            i = 1
            for index, entry in enumerate(self.historyLog, start=1):
                # Print details of each entry 
                print(f"Operation {index} -> {entry[0]} {entry[1]}\n")

    def visualize_parse_tree(self):
        """
        Visualizes the parse tree for a selected assignment statement.
        """
        try:
            # Get user input for the variable to visualize
            variable = input("Enter the variable to visualize parse tree: ")

            # Get the expression corresponding to the variable
            expression = self.__parse_tree.get_statements()[variable]  # Change here

            if not expression:
                raise ValueError(f'No parse tree available for variable "{variable}".')

            # Create a directed graph using networkx
            G = nx.DiGraph()
            self.__build_graph(G, expression)

            # Draw the graph using matplotlib
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='lightblue')
            plt.title(f"Parse Tree for Variable: {variable}")
            plt.show()

            # Log the history entry
            self.historyLog.append(("Visualized Parse Tree - Variable:", variable))

        except Exception as e:
            # Handle exceptions and print error messages
            print(f'\nAn error occurred: {e}')

    def __build_graph(self, G, expression):
        """
        Recursively builds a directed graph for the parse tree.
        """
        if expression:
            # Add the current node to the graph
            G.add_node(expression.key)  # Access the key attribute directly

            # Recursively build the graph for the left and right subtrees
            if expression.leftTree:
                G.add_edge(expression.key, expression.leftTree.key)  # Access the key attribute directly
                self.__build_graph(G, expression.leftTree)
            if expression.rightTree:
                G.add_edge(expression.key, expression.rightTree.key)  # Access the key attribute directly
                self.__build_graph(G, expression.rightTree)
   


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