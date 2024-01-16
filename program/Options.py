from ADT import Hashtable, Statement, SortedList
from utils import ParseTree
from utils import FileHandler

class Options:
    def __init__(self) -> None:
        # self.__hashtable = Hashtable()
        self.__parse_tree = ParseTree()

    # Getter function
    def get_saved_statements(self):
        return self.__parse_tree

    # Setter function
    def set_hashtable(self, new_hashtable:Hashtable):
        try:
            self.__parse_tree = new_hashtable
        except:
            return 'Set hash table failed'

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
        for key in self.__parse_tree.statements:
            
        sorted_statements = ''

        # Write to file
        file_handler = FileHandler()
        file_handler.write(output_file, sorted_statements)