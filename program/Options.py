class Options:
    def __init__(self) -> None:
        self.__saved_statements = {}

    # Getter function
    def get_saved_statements(self):
        return self.__saved_statements

    # Setter function
    def set_saved_statements(self, new_statements:dict):
        self.__saved_statements = new_statements

    def get_all_keys(self, saved_statements):
        return list(saved_statements.keys())
    
    def get_all_values(self, saved_statements):
        return list(saved_statements.values())
        
    def add_or_modify(self, statement):
        statement = statement.replace(" ", "")
        statement_split = statement.split('=')
        variable = statement_split[0]
        expression = statement_split[1]

        # Record new statement
        self.__saved_statements[variable] = expression