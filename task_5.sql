# Creating the task_5.sql file with the required SQL commands to insert a single row into the Customers table in alx_book_store database
sql_insert_content = """
-- Use the alx_book_store database
USE alx_book_store;

-- Insert a single row into the Customers table
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
"""

file_path = '/mnt/data/task_5.sql'
with open(file_path, 'w') as file:
    file.write(sql_insert_content)

file_path
