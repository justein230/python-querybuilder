# Python Query Builder Library

Welcome to the Python Query Builder library! This library is intended to make it easier to work with SQL queries based on a JSON file instead of a long string hard-coded inside of Python or a text file.

## Install the Query Builder library using the .whl file
1. Find the .whl file under Releases in GitHub and download the file.
2. Run the following command: `pip install <filename>.whl`

## How to use the Query Builder library
1. At the top of your Python file, add the following import: `from querybuilder import QueryBuilder`
2. Add your desired query in the JSON format provided to a JSON file of your choice.
3. In your code, call the QueryBuilder using the following parameters: `query = QueryBuilder(file_path, query_name)`
4. That is it! To get your query, call `query.get_query_string()`.

If you have any contributions or suggestions to the module, please don't hesitate to contribute! I made this to make my life easier for a project I was working on, and thought I would share. Any improvements are welcome!