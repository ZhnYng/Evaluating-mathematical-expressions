from ADT import Hashtable, Statement, SortedList
from utils import ParseTree
from utils import FileHandler

class Options:
    def __init__(self) -> None:
        # self.__hashtable = Hashtable()
        self.__parse_tree = ParseTree()

    # Getter function
    @property
    def parse_tree(self):
        return self.__parse_tree

    # Setter function
    @parse_tree.setter
    def parse_tree(self, new_parse_tree:ParseTree):
        try:
            self.__parse_tree = new_parse_tree
        except:
            return 'Set parse tree failed'

    def add_or_modify(self, statement:Statement):
        statement = Statement(statement)
        # Record new statement
        self.__parse_tree.add_statement(statement.var, statement.exp)

    def display_statements(self):
        statement_and_answers = {}
        for key in self.__parse_tree.statements:
            expression = self.__parse_tree.statements[key]
            statement = f"{key}={expression.return_tree()}"
            
            answer = self.__parse_tree.evaluate(key, expression)
            statement_and_answers[statement] = answer
        return statement_and_answers

    def eval_one_var(self, var:str):
        expression = self.__parse_tree.statements[var]
        expression.printPostorder(0)
        return self.__parse_tree.evaluate(var, expression)
    
    def read_from_file(self, file):
        sorted_list = SortedList()
        file_handler = FileHandler()

        statements = file_handler.read(file, read_mode='line')
        for statement in statements:
            statement = Statement(statement)
            sorted_list.insert(statement)
        
        for statement in sorted_list.items():
            self.add_or_modify(statement)

        return self.display_statements()
    
    def sorting_expressions(self, output_file):
        def custom_sort(item):
            equation, answer = item
            if answer == 'None':
                return (-float('-inf'), equation)
            return (-float(answer), equation)

        # Sort the dictionary based on the custom sorting key
        sorted_eqns = dict(sorted(self.display_statements().items(), key=custom_sort))
        swapped_dict = {}
        for key, value in sorted_eqns.items():
            if value not in swapped_dict:
                swapped_dict[value] = []
            swapped_dict[value].append(key)

        sorted_output = ''
        for answer, list_of_eqns in swapped_dict.items():
            formatted = f'\n*** Statements with value=> {answer}\n'
            for eqn in list_of_eqns:
                formatted += f'{eqn}\n'
            sorted_output += formatted

        # Write to file
        file_handler = FileHandler()
        file_handler.write(output_file, sorted_output)