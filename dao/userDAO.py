import pymysql
from dao import database  # Import the database connection utility

def getUser(userid):
    """Fetch a user from the database by user_id."""
    db = database.get_db_connection()  # Get a database connection
    if db:
        try:
            cursor = db.cursor()  # Initialize cursor
            query = "SELECT * FROM c_users WHERE user_id = %s"
            cursor.execute(query, (userid,))  # Use parameterized query to avoid SQL injection
            result = cursor.fetchone()  # Fetch the user record
            if result:
                return result  # Return user if found
            else:
                return None  # Return None if user is not found
        except pymysql.MySQLError as err:
            print(f"Error while fetching user: {err}")
            return None  # Return None if there is an error
        finally:
            cursor.close()  # Always close the cursor
            db.close()  # Close the database connection
    else:
        print("Failed to connect to the database.")
        return None  # Return None if connection fails

def createUser(user_id):
    """Add a new user to the c_users table."""
    db = database.get_db_connection()  # Get a database connection
    if db:
        try:
            cursor = db.cursor()  # Initialize cursor
            query = """
                INSERT INTO c_users (user_id)
                VALUES (%s)
            """
            cursor.execute(query, (user_id))  # Use parameterized query
            db.commit()  # Commit the changes to the database
            print(f"User added successfully with ID {user_id}.")
        except pymysql.MySQLError as err:
            print(f"Error while adding user: {err}")
        finally:
            cursor.close()  # Always close the cursor
            db.close()  # Close the database connection
