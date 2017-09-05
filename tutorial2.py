import sqlite3

# open the database
conn = sqlite3.connect('example.db')

# create a cursor object
cursor = conn.cursor()

# construct a query
# pass query to cursor.execute
cursor.execute('''
				SELECT * FROM stocks 
				''')

# iterate over the result

print(cursor.fetchone())
# for rec in cursor:
# 	print(rec)

conn.commit()
conn.close()