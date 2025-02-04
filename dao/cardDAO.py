import pymysql
from dao import database  # Import the database connection utility

def showRandomCard():
    db = database.get_db_connection()  # Get a database connection
    if db:
        try:
            cursor = db.cursor()  # Initialize cursor
            #get random number
            randomNumber = 2
            query = "SELECT * FROM c_cards WHERE card_id = %s"
            cursor.execute(query, (randomNumber,))  # Use parameterized query to avoid SQL injection
            result = cursor.fetchone()  # Fetch the card
            if result:
                return result  # Return card
            else:
                return None  # Return None if user is not found
        except pymysql.MySQLError as err:
            print(f"Error while fetching card: {err}")
            return None  # Return None if there is an error
        finally:
            cursor.close()  # Always close the cursor
            db.close()  # Close the database connection
    else:
        print("Failed to connect to the database.")
        return None  # Return None if connection fails