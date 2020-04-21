import sqlite3

def getQuote():

	#connecting to the database
    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()

    #fetching the SQL data from the database
    cur.execute("""
                SELECT * FROM quotes2 ORDER BY RANDOM() LIMIT 1;
                """)           
    try: 
        return cur.fetchall()
    finally:
        conn.close()

