# MySQLServer.py
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to the MySQL server
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost'
        )
        cursor = cnx.cursor()
        
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        # Handle errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()

if __name__ == "__main__":
    create_database()
