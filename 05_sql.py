# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT into populations values('NY City','NY',8400000)")
    cursor.execute("INSERT INTO populations VALUES('San cisco', 'CA', 800000)")

    # commit the changes
    conn.commit()

except sqlite3.OperationalError as error:
    print("Oops! Something went wrong. Try again", error)

# close the database connection
conn.close()
