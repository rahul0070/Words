from tkinter import *
from tkinter.ttk import *
import sqlite3

conx = sqlite3.connect("database_words.db")
def count_index():
    cur = conx.cursor()
    count = cur.execute("select count(word) from daily;")
    rowcount = cur.fetchone()[0]
    return rowcount

def enter(event=None):
    x=e1.get()
    y=e2.get()
    ci=count_index()+1
    conx.execute("insert into daily(id, word, meaning) values(?,?,?);",(ci,x,y))
    conx.commit()


s = Style()
s.configure('My.TFrame', background='khaki1', height=30, width=100)

s1=Style()
s1.configure('My.Label', background='LightCyan2', font=('Helvetica', 9, 'bold italic'))

fr =Frame(style='My.TFrame')
bt=Button(fr)
fr.pack(expand=YES)
l1=Label(fr, text="Enter word").grid(row=1,column=1)
l2=Label(fr, text="Enter meaning").grid(row=2,column=1)
e1=Entry(fr)
e2=Entry(fr)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e1.focus()
e2.focus()
bt.config(text="ENTER",command=enter)
bt.grid(row=3,column=2)
bt.bind('<Return>',enter)

fr.mainloop()
