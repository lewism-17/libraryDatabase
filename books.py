import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20)

        l1 = tk.Label(self,text="Welcome to the Libary", font=self.titlefont)
        l1.grid(row=0, column=0, columnspan=3, sticky = "EW")

        l2 = tk.Label(self, text = "Search by Title")
        l2.grid(row=1, column=0)
        self.titlesearchbox = tk.Entry(self, width = 28)
        self.titlesearchbox.grid(row=2, column = 0)

        l3 = tk.Label(self, text = "Search by Author")
        l3.grid(row=1, column=1)
        self.authorsearchbox = tk.Entry(self, width = 28)
        self.authorsearchbox.grid(row=2, column = 1)

        l4 = tk.Label(self, text = "Search by Year")
        l4.grid(row=1, column=2)
        self.yearsearchbox = tk.Entry(self, width = 28)
        self.yearsearchbox.grid(row=2, column = 2)
        

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass
