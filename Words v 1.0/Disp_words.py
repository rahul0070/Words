import sqlite3
from tkinter import *
from tkinter.ttk import *

s = Style()
s.configure('My.TFrame', background='DarkOliveGreen4')

fr=Frame(width=120, style='My.TFrame')
fr.pack(fill=Y)
l1=Label(fr, text="WORDS", font=("Helvetica", 16))
l1.pack()
scrollbar = Scrollbar(fr)
scrollbar.pack( side = RIGHT, fill = Y )
list = Listbox(fr, yscrollcommand = scrollbar.set, width=100, height=40, bg="DarkOliveGreen1", font = ("Helvetica", 12))

conn=sqlite3.connect("database_words.db")
cursor=conn.execute("select * from words;")
i=0
for row in cursor:
    list.insert(i,str(row[0])+". "+row[1]+" : "+row[2])
    list.insert(i+1, ' ')
    i=i+2
list.pack()
scrollbar.config(command=list.yview)


fr.mainloop()
