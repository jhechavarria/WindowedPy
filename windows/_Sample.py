import tkinter as tk
from windows._Window import _Window

class _Sample(_Window):

    def __init__(self, parent, controller):
        _Window.__init__(self, parent, controller)

        label = tk.Label(text="I am Sample Page label!")
        label.pack()

    def call(self, *args, **kwargs):
    	self.title("Window Title")
