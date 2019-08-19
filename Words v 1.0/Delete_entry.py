from tkinter import *
import sqlite3
list1 = []

x=input("Enter index of numbers:")
list1 = list(map(int, x.split()))
conn=sqlite3.connect("database_words.db")

def count_index():
    cur = conn.cursor()
    count = cur.execute("select count(word) from words;")
    rowcount = cur.fetchone()[0]
    return rowcount

ct=count_index()

def get_index():
    j=0
    index_list = []
    cursor=conn.execute("select * from words;")
    for row in cursor:
        index_list.append(row[0])
    return index_list


for x in list1:
 conn.execute("delete from words where id=?",(x,))
 conn.commit()

i_list=get_index()

for i in range(ct):
    conn.execute("update words set id=? where id=?",(i+1,i_list[i]))
    conn.commit()

print("WORDS DELETED")
