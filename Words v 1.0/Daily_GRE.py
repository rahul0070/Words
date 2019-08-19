import tkinter as tk
import sys

class App(tk.Tk):
   def __init__(self):
       super().__init__()
       self.create_scr()
        
    
   def run(self):
       self.mainloop()

   def create_scr(self):
       self.fr=tk.Frame(self, bg="springgreen")
       self.fr.pack(fill="x")

       l1=tk.Label(self.fr, text="DAILY WORDS", bg="springgreen", fg="black")
       l1.pack()

       b1=tk.Button(self.fr, text="OPEN APP", command=self.op, width=15, bg='Palegreen4')
       b1.pack()

       b5=tk.Button(self.fr, text="DISPLAY WORDS", command=self.dis, width=15, bg='Palegreen4')
       b5.pack()

       b3=tk.Button(self.fr, text="ADD WORDS", command=self.wd, width=15, bg='Palegreen4')
       b3.pack()

       b4=tk.Button(self.fr, text="RESET AND UPDATE", command=self.re, width=15, bg='Palegreen4')
       b4.pack()

       b2=tk.Button(self.fr, text="EXIT",command= self.exi, width=15, bg='Palegreen4')
       b2.pack()

   def op(self):
       import Main_app_daily

   def exi(self):
       sys.exit()

   def wd(self):
       import Enter_daily

   def re(self):
       import Reset_daily
   def dis(self):
       import Disp_daily

       
ob=App()
ob.run()
