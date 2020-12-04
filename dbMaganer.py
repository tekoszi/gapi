import sqlite3



conn = sqlite3.connect('database.db')
c = conn.cursor()
# args = {
#     "ip": "0.0.0.3",
#     "location": "Germany",
#     "symbol": "GER"
# }

# c.execute('''CREATE TABLE auth (token text)''')
# c.execute("INSERT INTO geo VALUES ('0.0.0.3','Poland','PL')")
#
# ip = ('0.0.0.5',)
#
# c.execute('SELECT * FROM geo WHERE ip=?', ip)
#
# updateData = (args['location'], args['symbol'], args['ip'])
# if c.fetchall():
#     print('someting')
# else:
#     print('nothing')

conn.commit()
c.execute('SELECT * FROM geo WHERE ip=?', ('0.0.0.1',))
print(c.fetchone())
conn.commit()

conn.close()