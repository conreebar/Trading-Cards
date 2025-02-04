# database.py
import pymysql

def get_db_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        db = pymysql.connect(
            host="127.0.0.1",      # Use host without port
            port=3306,             # Specify port as a separate parameter
            user="root",
            password="2323",
            database="trading_cards_db",  # Make sure the database is provided here
            cursorclass=pymysql.cursors.DictCursor
    )
        print("Database connection successful!")
        return db
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None
