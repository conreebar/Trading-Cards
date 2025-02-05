import pymysql
from dao import database

def getUser(userid):
    """Fetch a user from the database by user_id."""
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            query = "SELECT * FROM c_users WHERE user_id = %s"
            cursor.execute(query, (userid,))
            result = cursor.fetchone()
            if result:
                return result 
            else:
                return None  
        except pymysql.MySQLError as err:
            print(f"Error while fetching user: {err}")
            return None
        finally:
            cursor.close() 
            db.close()
    else:
        print("Failed to connect to the database.")
        return None 

def createUser(user_id):
    """Add a new user to the c_users table."""
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            query = """
                INSERT INTO c_users (user_id)
                VALUES (%s)
            """
            cursor.execute(query, (user_id)) 
            db.commit()  
            print(f"User added successfully with ID {user_id}.")
        except pymysql.MySQLError as err:
            print(f"Error while adding user: {err}")
        finally:
            cursor.close()
            db.close()  
