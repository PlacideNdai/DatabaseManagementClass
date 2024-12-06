import mysql.connector 
import pandas as pd 
from mysql.connector import Error 

file_loc = "./audience.csv"

dataframe = pd.read_csv(file_loc)

def insertData(df, tb):
    try:
        print("trying")
        conn = mysql.connector.connect(
            host='localhost', 
            user="root",
            password='Nopassword52!',
            database='poemdbfinal'
        )
        
        
        if conn.is_connected():
            cursor = conn.cursor()
            for i, row in df.iterrows():
                sql = f"insert into {tb} (first_name, last_name, email, gender,birthday,passwd) values(%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                conn.commit()
            print("Data posted!")
            
    except Error as e:
        print(e)
    finally: 
        if conn.is_connected():
            cursor.close()
            conn.close()
        

insertData(dataframe, 'audience')