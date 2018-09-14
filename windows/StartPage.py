import tkinter as tk
from tkinter import ttk
from windows._Window import _Window

class StartPage(_Window):

    def __init__(self, parent, controller):
        _Window.__init__(self, parent, controller)

        frm = tk.Frame(self)
        frm.pack(side="top", fill="both")

        btn1 = ttk.Button(frm, text="About Page >", command=lambda:self.goto("AboutPage"))
        btn1.pack(side="left", fill="both", expand=True)

        btn2 = ttk.Button(frm, text="Config Page >", command=lambda:self.goto("ConfigPage"))
        btn2.pack(side="right", fill="both", expand=True)

        lbl = ttk.Label(self, text="Welcome to My App!")
        lbl.pack(padx=10, pady=20)

    def call(self):
    	self.title("Start Page")
