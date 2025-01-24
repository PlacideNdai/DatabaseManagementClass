import mysql.connector 
import pandas as pd 
from mysql.connector import Error 

file_loc = "./buys.csv"

dataframe = pd.read_csv(file_loc)

def insertData(df, tb):
    try:
        print("trying")
        conn = mysql.connector.connect(
            host='localhost', 
            user="root",
            password='mypassword',
            database='poemdbfinal'
        )
        
        
        if conn.is_connected():
            cursor = conn.cursor()
            for i, row in df.iterrows():
                # sql = f"insert into {tb} (name,city, state, street, details, event_data) values(%s,%s,%s,%s,%s,%s)" #events 
                # sql = f"insert into {tb} (price, seatNumber) values(%s,%s)"
                sql = f'insert into {tb} (customerID, whenSold,ticketID) values(%s,%s,%s)' 
                cursor.execute(sql, tuple(row))
                conn.commit()
            print("Data posted!")
            
    except Error as e:
        print(e)
    finally: 
        if conn.is_connected():
            cursor.close()
            conn.close()
        

insertData(dataframe, 'buys')