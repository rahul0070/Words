from tkinter import *
from tkinter.ttk import *
import sqlite3
import os
import re

def search():
	li.delete(0, END)
	x = e1.get()
	conn = sqlite3.connect('database_words.db')
	i = 0
	x = (x + '*')
	cur = conn.execute('select * from words')
	for row in cur:
		result = re.match(x, row[1], re.IGNORECASE)
		if result:
			li.insert(i, str(row[0]) + '      ' + str(row[1]))
		i = i + 1



fr = Tk()
e1 = Entry(fr)
b1 = Button(fr, text = 'SUBMIT', command = search)
li = Listbox(fr)

e1.pack()
b1.pack()
li.pack()

fr.bind('<Return>', search)
fr.mainloop()
