# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    # use a for loop to iterate through the database, printing the results line by line
    cursor.execute("SELECT firstname, lastname from employees")

    rows = cursor.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])
