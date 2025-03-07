import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20)

        l1 = tk.Label(self,text="Welcome to the Libary", font=self.titlefont)
        l1.grid(row=0, column=0, columnspan=4, sticky = "EW")

        l2 = tk.Label(self, text = "Search by Title")
        l2.grid(row=1, column=0)
        self.titlesearchbox = tk.Entry(self, width = 18)
        self.titlesearchbox.grid(row=2, column = 0)

        l3 = tk.Label(self, text = "Search by Author")
        l3.grid(row=1, column=1)
        self.authorsearchbox = tk.Entry(self, width = 18)
        self.authorsearchbox.grid(row=2, column = 1)

        l4 = tk.Label(self, text = "Search by Year")
        l4.grid(row=4, column=0)
        self.yearsearchbox = tk.Entry(self, width = 18)
        self.yearsearchbox.grid(row=5, column = 0)
        
        l5 = tk.Label(self, text = "Search by Genre")
        l5.grid(row=4, column=1)
        self.genresearchbox = tk.Entry(self, width = 18)
        self.genresearchbox.grid(row=5, column = 1)

        l6 = tk.Label(self, text = "Available", font = self.titlefont)
        l6.grid(row = 6, column = 0, columnspan = 2, stick = "EW")

        l7 = tk.Label(self, text = "Your Collection", font = self.titlefont)
        l7.grid(row = 1, column = 2, columnspan = 2, stick = "EW")

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass
