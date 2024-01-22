from ADT import Hashtable, Statement, SortedList
from utils import ParseTree, FileHandler, MergeSort

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
        if expression:
            expression_tree_str = expression.printInOrder(0)
            return expression_tree_str, self.__parse_tree.evaluate(var, expression)
        else:
            raise ValueError('Expression does not exist.')
    
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
        if str(self.display_statements()) == '{}':
            raise ValueError('No statements to sort.')
            
        sorter = MergeSort(self.display_statements())
        sorter.merge_sort()
        sorted_dict = sorter.get_sorted_dict()

        sorted_output = ''
        for answer, list_of_eqns in sorted_dict.items():
            formatted = ''
            if sorted_output:
                formatted += '\n'
            formatted += f'*** Statements with value=> {answer}\n'
            for eqn in list_of_eqns:
                formatted += f'{eqn}\n'
            sorted_output += formatted

        # Write to file
        file_handler = FileHandler()
        file_handler.write(output_file, sorted_output)