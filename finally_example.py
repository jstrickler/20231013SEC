import sqlite3


db_conn = None
try:
    db_conn = sqlite3.connect('barfo.db')

    cursor = db_conn.cursor()
except sqlite3.InternalError as err:
    print(err)
    exit()
finally:
    if db_conn is not None:
        db_conn.close()


