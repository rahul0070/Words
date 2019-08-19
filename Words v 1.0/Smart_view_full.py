import sqlite3
from tkinter import *
from tkinter.ttk import *

def disp_meaning(i):
	word = list.get(ACTIVE)
	cur = conn.execute('select * from words')
	for j in cur:
		if j[1] == word:
			l2.config(text = j[2])

def se():
	import Search

s = Style()
s.configure('My.TFrame', background='snow')

fr=Frame(width=50)
fr.pack()
l1=Label(fr, text="WORDS", font=("Helvetica", 14))
l2 = Label(fr, font=('', 12))
l4 = Label(fr, text = 'MEANING', font=("Helvetica", 14))
scrollbar = Scrollbar(fr)
list = Listbox(fr, yscrollcommand = scrollbar.set, width=50, height=20, font = ("Helvetica", 12))
bx = Button(fr, text = 'SEARCH', command = se)

conn=sqlite3.connect("database_words.db")
cur = conn.execute("SELECT count(word) FROM words;")
count = cur.fetchone()[0]
print(count)
jk = 1
if jk == 1:
	cursor=conn.execute("select * from words;")
	i = 0
	for row in cursor:
		list.insert(i, row[1])
		i = i+1
	list.bind('<Double-1>', disp_meaning)    
	scrollbar.config(command=list.yview)

scrollbar.pack( side = RIGHT, fill = Y)
l4.pack()
l2.pack()
bx.pack()
l1.pack()
list.pack()


fr.mainloop()
