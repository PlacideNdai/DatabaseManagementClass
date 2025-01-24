import mysql.connector

# Database connection details
db_connection = {
    'user': 'root',
    'password': 'passwordhere',
    'host': 'localhost',
    'database': 'poemdbfinal',
    'port': '3306'
}

# Disconnecting from the DB
def disConnect(conn):
    if conn.is_connected():
        conn.close()
    print("Disconnected from the database. Bye!")

# Function to select from a single table
def selectFromTable(conn):
    arr = ["artist", "audience", "buys", "events", "genra", "poems", "tags", "tickets", "manages"]
    print("\nChoose a table to select from:")
    for i, table in enumerate(arr, 1):
        print(f"{i}) {table.capitalize()}")
    try:
        choose = int(input("Enter your choice (1-9): "))
        if 1 <= choose <= 9:
            table_name = arr[choose - 1]
            cursor = conn.cursor()
            query = f"SELECT * FROM {table_name} LIMIT 100;" 
            cursor.execute(query)
            results = cursor.fetchall()
            print(f"\nResults from {table_name.capitalize()}:")
            for row in results:
                print(row)
            cursor.close()
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
    except ValueError:
        print("Please enter a valid integer.")
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")

# Function to perform an update
def updatearow(conn):
    try:
        table_name = input("Enter the table name where you want to update a row: ")
        column = input("Enter the column to update: ")
        new_value = input("Enter the new value: ")
        condition = input("Enter the condition (e.g., id=1): ")
        query = f"UPDATE {table_name} SET {column} = %s WHERE {condition};"
        cursor = conn.cursor()
        cursor.execute(query, (new_value,))
        conn.commit()
        print(f"{cursor.rowcount} row(s) updated successfully.")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error updating row: {err}")

# Function to select with an inner join
def selectWithJoin(conn):
    try:
        table1 = input("Enter the first table name: ")
        table2 = input("Enter the second table name: ")
        join_condition = input("Enter the join condition (e.g., table1.id = table2.table1_id): ")
        query = f"SELECT * FROM {table1} INNER JOIN {table2} ON {join_condition} LIMIT 5;"
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(f"\nResults from the join between {table1} and {table2}:")
        for row in results:
            print(row)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error executing join query: {err}")

# Function to perform a GROUP BY query
def groupByCount(conn):
    try:
        table_name = input("Enter the table name: ")
        column = input("Enter the column to group by: ")
        query = f"SELECT {column}, COUNT(*) AS count FROM {table_name} GROUP BY {column};"
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(f"\nGrouped results from {table_name}:")
        for row in results:
            print(row)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error executing group by query: {err}")

# Main program logic
try:
    conn = mysql.connector.connect(**db_connection)
    if conn.is_connected():
        print("Database is ready!\n")
        # Main menu for commands
        commend = int(input("""Choose a command below: 
        1) Select from tables
        2) Select from two tables with inner join
        3) Group by count(*)
        4) Update
        5) Exist\nYour choice: """))

        if commend == 5:
            disConnect(conn)

        elif commend == 2:
            selectWithJoin(conn)

        elif commend == 3:
            groupByCount(conn)

        elif commend == 4:
            updatearow(conn)

        elif commend == 1:
            selectFromTable(conn)

        else:
            print("Invalid command. Please choose a number between 1 and 5.")

except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
