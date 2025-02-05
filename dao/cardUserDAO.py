from dao import database
import pymysql

def assignCardToUser(card_id, user_id):
    print(f'{card_id},{user_id}')
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            query = """
    INSERT INTO c_user_cards (user_id, card_id)
    VALUES (%s, %s)
    """
            cursor.execute(query, (user_id, card_id))
            db.commit() 
            
        except pymysql.MySQLError as err:
            print(f"Error while joining card to user: {err}")
            return None  # Return None if there is an error
        finally:
            cursor.close()  # Always close the cursor
            db.close()  # Close the database connection

    else:
        print("Failed to connect to the database.")
        return None
    