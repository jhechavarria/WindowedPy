import tkinter as tk
from tkinter import messagebox as msg

class _Window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

    def goto(self, frame, *args, **kwargs):
        self.controller.show_window(frame, *args, **kwargs)

    def title(self, text=None, sep=' - ', overwrite=False):
        self.controller.title(text, sep, overwrite)

    def message(self, text, title="Info", type="info"):
    	types = {
    		'info': msg.showinfo,
    		'warning': msg.showwarning,
    		'error': msg.showerror
    	}
    	if (type in types):
    		types[type](title, text)

    def question(self, text, title="Question"):
    	return msg.askquestion(title, text)

    def confirm(self, text, title="Question"):
    	return msg.askokcancel(title, text)
