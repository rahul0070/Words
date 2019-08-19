import tkinter as tk
from random import randint
import sqlite3


class Appd(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily")

        self.word_str = ''
        self.meaning_str = ''
        self.random_mem = 0
        self.attempt = 0
        self.li = []
        self.complete = []

        self.create_widgets()
        self.db_connect()

        for i in range(self.rowcount):
            self.li.append(4)

        self.display_next_word()

    def run(self):
        self.mainloop()

    def create_widgets(self):
        self.l1 = tk.Label(self, width=30, font=('Helvetica', 12))
        self.l1.grid(row=2, column=2)

        self.l2 = tk.Label(self)
        self.l2.grid(row=3, column=1, columnspan=3)

        self.l3 = tk.Label(self, width=30)
        self.l3.grid(row=5, column=1, columnspan=3)

        b1 = tk.Button(self, text="NEXT", command=self.display_next_word, height=2, width=10)
        b1.grid(row=4, column=1)

        b2 = tk.Button(self, text="MEANING", command=self.display_meaning, width=20, height=2)
        b2.grid(row=4, column=2)

        b3 = tk.Button(self, text="EXIT", command=self.destroy, width=10, height=2)
        b3.grid(row=4, column=3)

    def count_score(self):
        s4 = 0
        s5 = 0
        for so in self.li:
            if int(so) == 5:
                s5 = s5 + 1
            elif int(so) == 4:
                s4 = s4 + 1
        print('------- 5 = ', s5, ' -------')
        print('------- 4 = ', s4, ' -------')

    def db_connect(self):
        self.conn = sqlite3.connect("database_words.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT count(word) FROM words;")
        self.rowcount = self.cursor.fetchone()[0]

    def db_get_word(self):
        x = randint(0, self.rowcount - 1)
        while x == self.random_mem:
            x = randint(1, self.rowcount)
        self.random_mem = x
        # use SQL to get one row
        self.cursor.execute("SELECT * FROM words WHERE id = ?;", (self.random_mem + 1,))
        row = self.cursor.fetchone()
        self.word_str = row[1]
        self.meaning_str = row[2]

    # self.random_mem = self.random_mem-1

    # TODO: maybe you should use SQL to get random row
    # SELECT * FROM words ORDER BY RANDOM() LIMIT 1;
    # or
    # SELECT * FROM words WHERE id <> ? ORDER BY RANDOM() LIMIT 1; , random_mem

    def display_next_word(self):
        self.db_get_word()
        flag3 = 1
        while flag3 == 1:
            flag3 = 0
            for xi in self.complete:
                print(self.complete)
                if xi == self.random_mem:
                    flag3 = 1
                    self.db_get_word()
        print('out')
        self.l1['text'] = self.word_str
        self.l2['text'] = ''
        if self.li[self.random_mem] < 5:
            self.li[self.random_mem] = self.li[self.random_mem] + 1

        flag = 1
        for o in self.li:
            if o != 5:
                flag = 0
        if flag == 1:
            self.end_program()
        print(self.li)
        self.count_score()
        self.attempt = self.attempt + 1
        self.complete.append(self.random_mem)

    def end_program(self):
        self.l1['text'] = 'COMPLETED'

    def display_meaning(self):
        self.l2['text'] = self.meaning_str
        self.li[self.random_mem] = self.li[self.random_mem] - 2
        self.complete.remove(self.random_mem)


wi = Appd()
wi.run()
