import sqlite3
conn = sqlite3.connect('librarydatas.db')
cur = conn.cursor()
sql = "create table if not exists student(fname text,lname text, gender text,email text,department text,passwords text);"
sql1 = "create table if not exists teacher(fname text,lname text, gender text,email text,department text,passwords text);"

cur.execute(sql)
cur.execute(sql1)
conn.commit()
cur.close()


