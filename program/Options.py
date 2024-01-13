from ADT import Expression, Hashtable
from utils import ParseTree

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

    def add_or_modify(self, statement):
        statement = statement.replace(" ", "")
        statement_split = statement.split('=')
        variable = statement_split[0]
        expression = statement_split[1]

        # Record new statement
        self.__parse_tree.add_statement(variable, expression)

    def display_statements(self):
        statement_and_answers = {}
        for key in self.__parse_tree.statements:
            expression = self.__parse_tree.statements[key]
            statement = f"{key}={expression.shallow_tree()}"
            
            answer = self.__parse_tree.evaluate(key, expression)
            statement_and_answers[statement] = answer
        return statement_and_answers
    
# a=(1+b)
# b=(1+6)