import pymysql
from dao import database

def getCardByName(card_name):
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            query = "SELECT * FROM c_cards WHERE card_name = %s"
            cursor.execute(query, (card_name,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return None
        except pymysql.MySQLError as err:
            print(f"Error while fetching card: {err}")
            return None
        finally:
            cursor.close()
            db.close() 

    else:
        print("Failed to connect to the database.")
        return None
    
def showRandomCard():
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()

            #TODO return random number between 1 and maxvalue
            randomNumber = 2
            query = "SELECT * FROM c_cards WHERE card_id = %s"
            cursor.execute(query, (randomNumber,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return None 
        except pymysql.MySQLError as err:
            print(f"Error while fetching card: {err}")
            return None
        finally:
            cursor.close()  
            db.close() 
    else:
        print("Failed to connect to the database.")
        return None  