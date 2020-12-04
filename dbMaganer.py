import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()


# c.execute('''CREATE TABLE geo (ip text, location text, symbol text)''')
# c.execute("INSERT INTO geo VALUES ('0.0.0.0','Poland','PL')")
# c.execute("INSERT INTO geo VALUES ('0.0.0.1','Poland','PL')")
conn.commit()
c.execute("SELECT * FROM geo")
print(c.fetchall())
conn.close()