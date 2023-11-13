
import sqlite3

# conn = sqlite3.Connection(...)
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    cursor = conn.cursor()  # get a cursor object

    # select first name, last name from all presidents
    cursor.execute('''
        select *
        from presidents
    ''')  # execute a SQL statement

    print("Sqlite3 does not provide a row count\n")  # (included for consistency with other DBMS modules)

    for row in cursor.fetchall():  # fetchall() returns all rows
        print(row)
#        print(' '.join(row))  # each row is a tuple

