import psycopg2 
#from psycopg2 import sql   

#def db_access(): 
try:
    connection = psycopg2.connect(database='first_database', 
                                    user='postgres', 
                                    password='admin', 
                                    host='localhost', 
                                    port='5432') 
    cursor = connection.cursor()  
    sql = '''CREATE DATABASE'''; 
    print('Created database succesfully') 
    cursor.execute(sql)  
    connection.close() 
    #return execution       
        
except Exception as error: 
    print(f'error occured: {error}') 
    
#db_access() 