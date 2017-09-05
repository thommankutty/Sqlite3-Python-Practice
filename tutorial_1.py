"""
This is a script written to learn the sqlite3 module in python
"""

# import modules
import sqlite3

# establish connection
conn = sqlite3.connect('example.db')

# create cursor object
c = conn.cursor()

# execute the cursor
c.execute('''
			CREATE TABLE IF NOT EXISTS stocks
			 (date TEXT, trans TEXT, symbol TEXT, rty REAL, price REAL)
			''')

# insert data into the table

# insert many
# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

c.executemany('''
				INSERT INTO stocks VALUES(?,?,?,?,?)
				''', purchases)

# commit the connection
conn.commit()

# close the connection
conn.close()