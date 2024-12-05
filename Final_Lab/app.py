import mysql.connector 

db_connection = {
    'user':'root',
    'password':'Nopassword52!',
    'host': 'localhost', 
    'database': 'poemdbfinal',
    'port':'3306'
}

# Disconnecting from the DB
def disConnect(conn):
    if conn.is_connected():
        conn.close()
    print("bye..")
    


try:
    conn = mysql.connector.connect(**db_connection)
    if conn.is_connected():
        print("Database is ready!\n")
        # THE WORKS GOES HERE 
        while True:
            commend = int(input("""choose a command below: \n
            1) simple select 
            2) select from more than 1 table  
            3) subquery function  
            4) Group by 
            5) Update 
            6) Exist\n """))
            
            if commend == 6:
                disConnect(conn)
                break
            
            elif commend == 2:
                print("select from 2 or more tables")
            
            elif commend == 3:
                print("subquery select")
                
            elif commend == 4:
                print("Group by")
                
            elif commend == 5: 
                print("Update")
                
            else:
                print('Simple Select:\n Available Tables \n artist \ngenra')
                
    
except mysql.connector.Error as err:
    print(f"Database connection error: {err}");
