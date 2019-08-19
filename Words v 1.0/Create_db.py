import sqlite3
import sys
import os

x=input("Enter password to continue:")
if x!='myapp':
   e=input("WRONG PASSWORD")
   sys.exit()
#os.remove("database_words.db")
conn=sqlite3.connect('database_words.db')

conn.execute("create table words(id number, word varchar(25), meaning varchar(150));")
conn.execute("create table daily(id number, word varchar(25), meaning varchar(150));")
