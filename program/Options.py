from ADT import Expression, Hashtable

class Options:
    def __init__(self) -> None:
        self.__hashtable = Hashtable()

    # Getter function
    def get_saved_statements(self):
        return self.__hashtable

    # Setter function
    def set_hashtable(self, new_hashtable:Hashtable):
        try:
            self.__hashtable = new_hashtable
        except:
            return 'Set hash table failed'

    def add_or_modify(self, statement):
        statement = statement.replace(" ", "")
        statement_split = statement.split('=')
        variable = statement_split[0]
        expression = Expression(statement_split[1])

        # Record new statement
        self.__hashtable[ord(variable)] = expression

    def display_statements(self):
        statement_and_answers = {}
        for key in self.__hashtable:
            expression = self.__hashtable[key]
            statement = f"{chr(key)}={expression}"
            statement_and_answers[statement] = expression.get_solution()
        return statement_and_answers