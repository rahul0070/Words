import sqlite3
from tkinter import *

conn=sqlite3.connect("database_words.db")

file_ob = open("GRE_words.txt", 'a')


def nw():
    file_ob.seek(0)
    file_ob.truncate()
    cursor = conn.execute("select * from words;")
    i = 0
    for row in cursor:
        file_ob.write(str(row[0]) + "." + str(row[1]) + ":" + str(row[2]))
    print('*FILE READY*')

fr=Frame()
fr.pack()
l1=Label(fr, text="Do you want to copy the contents to a file?").pack()
b2=Button(fr, text="NEW FILE", command=nw).pack()
print("*FILE READY*")
fr.mainloop()


