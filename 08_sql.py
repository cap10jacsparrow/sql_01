import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    try:
        c.execute("DROP TABLE if exists regions")
        c.execute("""CREATE TABLE regions
        (city TEXT, region TEXT)
        """)
        # (again, copy and paste the values if you'd like)
        cities = [
            ('New York City', 'Northeast'),
            ('San Francisco', 'West'),
            ('Chicago', 'Midwest'),
            ('Houston', 'South'),
            ('Phoenix', 'West'),
            ('Boston', 'Northeast'),
            ('Los Angeles', 'West'),
            ('Houston', 'South'),
            ('Philadelphia', 'Northeast'),
            ('San Antonio', 'South'),
            ('San Diego', 'West'),
            ('Dallas', 'South'),
            ('San Jose', 'West'),
            ('Jacksonville', 'South'),
            ('Indianapolis', 'Midwest'),
            ('Austin', 'South'),
            ('Detroit', 'Midwest')
        ]
        c.executemany("INSERT INTO regions VALUES(?, ? )", cities)
        c.execute("SELECT * FROM regions ORDER BY region DESC")
        rows = c.fetchall()
        for r in rows:
            print(r[0], r[1])
    except sqlite3.OperationalError as error:
        print(error, "occurred")
