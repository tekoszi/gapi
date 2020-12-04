import jwt

encoded_jwt = jwt.encode({'dominik': 'password'}, 'secret', algorithm='HS256').decode("utf-8")
print(encoded_jwt)

print(jwt.decode(encoded_jwt.encode("utf-8"), 'secret', algorithms=['HS256']))



import sqlite3



conn = sqlite3.connect('database.db')
c = conn.cursor()
# args = {
#     "ip": "0.0.0.3",
#     "location": "Germany",
#     "symbol": "GER"
# }

# c.execute('''CREATE TABLE auth (token text)''')
c.execute(r"INSERT INTO auth VALUES ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkb21pbmlrIjoicGFzc3dvcmQifQ.qq5UOReD2zE3p3f5LDwdjedmhqGMPQb-na0c-bWLjGo')")
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
c.execute('SELECT * FROM auth')
print(c.fetchall())
conn.commit()

conn.close()