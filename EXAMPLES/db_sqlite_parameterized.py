
import sqlite3

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    party_query = '''
    select firstname, lastname
    from presidents
        where party = ?
    '''  # ? is SQLite3 placeholder for SQL statement parameter; different DBMSs use different placeholders

    for party in 'Federalist', 'Whig':
        print(party)
        s3cursor.execute(party_query, (party,))  # second argument to execute() is iterable of values to fill in placeholders from left to right
        print(s3cursor.fetchall())
        print()
