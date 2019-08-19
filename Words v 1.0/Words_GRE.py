import tkinter as tk
import sys


class Appw(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_scr()

    def run(self):
        self.fr.mainloop()

    def create_scr(self):

        self.fr= tk.Frame(self, bg="dodgerblue" ,height=20, width=20)
        self.fr.pack(fill="x")

        l1 = tk.Label(self.fr, text="WORDS", bg="dodgerblue", fg="white")
        #l1.grid(row=2, column=1)
        l1.pack()

        b1 = tk.Button(self.fr, text="OPEN APP", command=self.op, width=15, bg="lightblue1")
        #b1.grid(row=3, column=1)
        b1.pack()

        b3 = tk.Button(self.fr, text="ADD WORDS", command=self.wd, width=15, bg="lightblue1")
        #b3.grid(row=4, column=1)
        b3.pack()

        b2 = tk.Button(self.fr, text="EXIT", command=self.exi, width=15, bg="lightblue1")
        #b2.grid(row=5, column=1)
        b2.pack()

    def op(self):
        import Main_app_words

    def exi(self):
        sys.exit()

    def wd(self):
        import Enter_words



ob = Appw()
ob.run()
