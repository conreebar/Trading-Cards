import random
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
    
def getRandomCardByRarity(rarity):
    db = database.get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            if rarity == "Legendary":
                query = """
                    SELECT * 
                    FROM c_cards 
                    WHERE rarity = %s 
                    AND (is_collected_legend != 1 OR is_collected_legend IS NULL)
                """
            else:
                query = """
                    SELECT * 
                    FROM c_cards 
                    WHERE rarity = %s
                """
            cursor.execute(query, (rarity,))
            results = cursor.fetchall()  # Fetch all matching cards

            if results:    
                random_card = random.choice(results)

                # If the chosen card is legendary, update `is_collected_legend` to 1
                if rarity == 'Legendary' and random_card['is_collected_legend'] is None:
                    update_query = """
                        UPDATE c_cards
                        SET is_collected_legend = 1
                        WHERE card_id = %s
                    """
                    cursor.execute(update_query, (random_card['card_id'],))
                    db.commit()  # Commit the change to the database

                return random_card
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