import importlib
import pkgutil
import sys
import tkinter as tk
import windows

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.wd_title = None

    def center_window(self, wdX=640, wdY=480):
        scX=self.winfo_screenwidth()
        scY=self.winfo_screenheight()
        posX=(scX // 2) - (wdX // 2)
        posY=(scY // 2) - (wdY // 2)

        self.geometry("{}x{}+{}+{}".format(wdX, wdY, posX, posY))

    def show_window(self, frame, *args, **kwargs):
        if frame in self.frames:
            self.frames[frame].call(*args, **kwargs)
            self.frames[frame].tkraise()
        else:
            print("Window not found: " + frame)
            sys.exit(1)

    def load_windows(self):
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for importer, modname, ispkg, in pkgutil.iter_modules(windows.__path__):
            if modname[0] in '_' or ispkg:
                continue
            mod = importlib.import_module("windows." + modname)
            try:
                cls = getattr(mod, modname)
                frame = cls(container, self)
            except:
                print('Error occured while loading window: ' + modname)
                sys.exit(1)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[modname] = frame

    def title(self, text=None, sep=' - ', overwrite=False):
        if text == None:
            return tk.Tk.title(self)
        else:
            if self.wd_title == None:
                self.wd_title = text
                tk.Tk.title(self, text)
            else:
                if overwrite:
                    tk.Tk.title(self, text)
                else:
                    tk.Tk.title(self, "{}{}{}".format(self.wd_title, sep, text))

app = App()
app.center_window()
app.title("MyApp")
app.load_windows()
app.show_window("StartPage")
app.mainloop()
