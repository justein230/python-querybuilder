import json

class QueryBuilder(object):

    def __init__(self, db_queries_file_path: str, query_name: str):
        db_query_file = json.load(open(db_queries_file_path, 'r'))
        self.columns = db_query_file[query_name]['columns']
        self.main_table_name = db_query_file[query_name]['table_name']
        self.joins = db_query_file[query_name]['joins']
        self.where_clause = db_query_file[query_name]['where']

    def get_columns_string(self):
        return ', '.join(self.columns)

    def get_joins_string(self):
        return ' '.join(self.joins)

    def get_query_string(self):
        return f"SELECT {self.get_columns_string()} FROM {self.main_table_name} {self.get_joins_string()} WHERE {self.where_clause}"