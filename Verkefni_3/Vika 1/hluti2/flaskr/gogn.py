#Ágúst Örn Eiðsson
#15.2.18

import sqlite3

with sqlite3.connect("gogn.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS entries (
  id integer primary key autoincrement,
  title text not null,
  "text" text not null);''')