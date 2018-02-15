#Ágúst Örn Eiðsson
#13.2.18

import sqlite3

with sqlite3.connect("gogn.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute('''
INSERT INTO USERS(username,firstname,lastname,password)
VALUES ("test_user","Páll","Guðmundsson","qwert")
''')
db.commit()

cursor.execute("SELECT * FROM USERS")

print(cursor.fetchall())