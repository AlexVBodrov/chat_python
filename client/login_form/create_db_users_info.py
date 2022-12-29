import sqlite3
import sys

# sys.path.append('../')

# create connection to
conn = sqlite3.connect('client/users_info.db')

# create cursor for
cur = conn.cursor()

# create table
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   username TEXT,
   password TEXT);""")

# save to database
conn.commit()

# insert values into database
cur.execute("""INSERT INTO users(userid, username, password) 
   VALUES('00001', 'Alex', '1234');""")
cur.execute("""INSERT INTO users(userid, username, password) 
   VALUES('00002', 'Lena', '12345');""")

# save to database
conn.commit()