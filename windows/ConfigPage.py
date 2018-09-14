import tkinter as tk
from tkinter import ttk
from windows._Window import _Window

class ConfigPage(_Window):

    def __init__(self, parent, controller):
        _Window.__init__(self, parent, controller)

        btn = ttk.Button(self, text="< Start Page", command=lambda:self.goto("StartPage"))
        btn.pack(side="top", fill="both")

        msg = tk.Message(self, text="This is a Tkinter message widget. Pretty exiting, huh? I enjoy Tkinter. It is very simple.")
        msg.pack(padx=10, pady=20, fill="both")
        msg.bind("<Configure>", lambda e: msg.configure(width=e.width-10))

        lbl = tk.Label(self, text="Change application style")
        lbl.pack()

        style = ttk.Style()
        for name in style.theme_names():
        	btn = ttk.Button(self, text=name, command=lambda: style.theme_use(name))
        	btn.pack()

    def call(self):
    	self.title("Config Page")
