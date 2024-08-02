import pymssql
import mysql.connector

# MySQL connection
mysql_conn = mysql.connector.connect(user="user", port=3306, passwd="", db="DBmane", host="mysqlhost") 

mysql_cursor = mysql_conn.cursor()

# SQL Server connection
sql_server_conn = pymssql.connect(server='Sql Host',
                                   user='username',
                                   password='',
                                   database='Dbname')

sql_server_cursor = sql_server_conn.cursor()



# Clone tables

sql_server_cursor.execute("SELECT name FROM sys.tables")
tables = sql_server_cursor.fetchall()

for table in tables:
    table_name = table[0]
    sql_server_cursor.execute(f"SELECT * FROM {table_name}")
    columns = [column[0] for column in sql_server_cursor.description]
    columns_str = ", ".join([f"{column} LONGTEXT" for column in columns])
    placeholders = ", ".join(['%s' for _ in columns])
    
    mysql_cursor.execute(f"CREATE TABLE {table_name} ({columns_str})")
    
    for row in sql_server_cursor.fetchall():
        mysql_cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", [str(value) for value in row])
      
# Commit changes and close connections
mysql_conn.commit()

sql_server_cursor.close()
sql_server_conn.close()

mysql_cursor.close()
mysql_conn.close()


change to exisute for only one table