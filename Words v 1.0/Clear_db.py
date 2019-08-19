import sqlite3
import sys

conn=sqlite3.connect("database_words.db")
x=input("Are you sure you want to delete?(y/n):")
if x=='y':
    conn.execute("delete from words;")
    conn.commit()
else:
    sys.exit()
