import os

class Interface:
    """
    This class represents the user interface/GUI for the 
    Evaluating & Sorting Assignment Statements (using parse trees) application.
    It provides various options for evaluating solutions, altering variables, and flexible evalutations.
    """
    def banner(self):
        """
        Prints the introductory banner for the application.
        """
        print('*'*65)
        print('* ST1507 DSAA: Evaluating & Sorting Assignment Statements ', ' '*4, '*')
        print('*', '-'*61, '*')
        print('*', ' '*61, '*')
        print('* - Done by: Lim Zhen Yang (2214506) & Ashley Bai (2237871)', ' '*3, '*')
        print('* - Class DAAA/FT/2B04', ' '*40, '*')
        print('*'*58, end='\n\n\n')

    def pause(self):
        """
        Pauses the program execution and waits for user input to continue.
        """
        print('')
        return os.system('pause')

    # Option 1
    def option1(self, add_or_modify):
        """
        Executes the first option in the menu: add or modify an assignment statement.
        """
        statement = input(f"Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
        result = add_or_modify(statement)
        self.pause()

    # Option 2
    def option2(self, display_statements):
        print(f"\nCURRENT ASSIGNMENTS:\n{'*'*20}")
        statement_and_answers = display_statements()
        for statement, answer in statement_and_answers.items():
            print(f"{statement}=> {answer}")
        self.pause()
        
    # Option 3
    def option3(self, eval_one_var):
        """
        Evaluates and prints a parse tree of an individual variable.
        """
        # Get user input for the variable to be evaluated
        variable = input("Please enter the variable you want to evaluate:\n")
        # Evaluate the specified variable using the eval_one_var function
        result = eval_one_var(variable)

        # Print result
        print(f"Value for variable \"{variable}\" is {result}\n")

        # Print additional message
        input("Press enter key, to continue...\n")
        
        
    # Option 4
    # def option4(self):