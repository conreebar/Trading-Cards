# database.py
import pymysql

def get_db_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        db = pymysql.connect(
            host="127.0.0.1",
            port=3306,            
            user="root",
            password="2323",
            database="mysql",
            cursorclass=pymysql.cursors.DictCursor
    )
        print("Database connection successful!")
        return db
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None
