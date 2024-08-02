This Python script transfers data from SQL Server database to a corresponding tables in a MySQL database. It includes the following steps:


Fetch Columns: Retrieve the column names and types from the SQL Server table.
Create Table in MySQL: Create a new table in the MySQL database with the same columns.
Insert Data: Fetch all rows from the SQL Server table and insert them into the MySQL table.
Commit Changes: Commit the transaction and close the database connections.
To use this script, replace 'your_table_name' with the actual name of the table you want to transfer. The script ensures the table structure and data are replicated accurately from SQL Server to MySQL.

Requirements
Python
pyodbc for SQL Server connection
mysql-connector-python for MySQL connection
