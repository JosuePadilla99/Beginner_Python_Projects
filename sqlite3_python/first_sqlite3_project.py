############################################### 
# Sqlite3 Databse 
# Creator: Josue Padilla 
# Created: 12/22/2024 
###############################################  

import sqlite3 
from tabulate import tabulate 



try:  
    connection = sqlite3.connect("my_first_database.db")
    print(f'Opened SQLite database file with {sqlite3.sqlite_version}')  
    cursor = connection.cursor()   
    new_connection = sqlite3.connect('new_database.db') 
    new_cursor = new_connection.cursor()  
    
    # Loop through all the tables and copy the data
    new_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") 
    tables = cursor.fetchall() 
    for table in tables: 
        table_name = table[0] 
        print(f'copying table: {table_name}')  
        
        #Get the table schema and recreate it in the new database
        cursor.execute(f"SELECT sql FROM sql_master WHERE name='{table_name}';") 
        create_table_sql = cursor.fetchone()[0] 
        new_cursor.execute(create_table_sql)  
        
        #Copying dtaa to the new database
        cursor.execute(f"SELECT * FROM {table_name}") 
        rows = cursor.fetchall() 
        #placeholders = ",".join() 
        new_cursor.executemany(f"INSERT INTO {table_name} VALUES", rows)
        
    #cursor.execute('''CREATE TABLE IF NOT EXISTS personal (First Name, Last Name, Birthday, Age)''') 
    #rows = cursor.execute("INSERT INTO personal VALUES('Josue', 'Padilla', '05-12-1999', '25')")
    #print(tabulate(rows, headers=['ID', 'First Name', 'Josue'], tablefmt='pretty'))
    new_connection.commit()      
    new_connection.close()  
    
except sqlite3.OperationalError as error: 
        print('failed to open database. Error_code:', error)    