import pymysql
from dao import database

def aiRunQuery(query):
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
            else:
                return None
        except pymysql.MySQLError as err:
            print(f"Error while AI talked to server: {err}")
            return None
        finally:
            cursor.close()
            db.close() 

    else:
        print("Failed to connect to the database.")
        return None