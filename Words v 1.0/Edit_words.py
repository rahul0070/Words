import sqlite3
from tkinter import *
from tkinter.ttk import *

def disp_meaning(i):
	e1.delete(0, END)
	global word
	word = list.get(ACTIVE)
	cur = conn.execute('select * from words')
	for j in cur:
		if j[1] == word:
			e1.insert(0, j[2])
	e1.focus()		

def edit():
	conn.execute('update words set meaning=? where word=?',(e1.get(), word))
	conn.commit()
	conn.close()


def search():
	list.delete(0, END)
	x = e2.get()
	conn = sqlite3.connect('database_words.db')
	i = 0
	x = (x + '*')
	cur = conn.execute('select * from words')
	for row in cur:
		result = re.match(x, row[1], re.IGNORECASE)
		if result:
			list.insert(i, str(row[1]))
		i = i + 1	
	


s = Style()
s.configure('My.TFrame', background='snow')

fr=Frame(width=70)
fr.pack()
l1=Label(fr, text="WORDS", font=("Helvetica", 14))
e1 = Entry(fr, font=('', 12), width = 50)
l4 = Label(fr, text = 'MEANING', font=("Helvetica", 14))
scrollbar = Scrollbar(fr)
list = Listbox(fr, yscrollcommand = scrollbar.set, width=50, height=20, font = ("Helvetica", 12))
b1 = Button(fr, text = 'EDIT', command = edit)
e2 = Entry(fr)
b2 = Button(fr, text = 'SUBMIT', command = search)


conn=sqlite3.connect("database_words.db")
cursor=conn.execute("select * from words;")
i=0
for row in cursor:
    list.insert(i, row[1])
    i=i+1
list.bind('<Double-1>', disp_meaning)
fr.bind('<Return>', edit)    
scrollbar.config(command=list.yview)


scrollbar.pack( side = RIGHT, fill = Y)
l4.pack()
e1.pack()
b1.pack()
e2.pack()
b2.pack()
l1.pack()
list.pack()


fr.mainloop()
