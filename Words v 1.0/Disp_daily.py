import sqlite3
from tkinter import *
from tkinter.ttk import *

fr=Frame()
fr.pack(fill=Y)
scrollbar = Scrollbar(fr)
scrollbar.pack( side = RIGHT, fill = Y )
list = Listbox(fr, yscrollcommand = scrollbar.set )
list.config(width=100)
conn=sqlite3.connect("database_words.db")
cursor=conn.execute("select * from daily;")
i=0
for row in cursor:
    list.insert(i,str(row[0])+". "+row[1]+" : "+row[2])
    i=i+1
list.pack(side = LEFT, fill = Y )
scrollbar.config(command=list.yview)


fr.mainloop()
