import tkinter
import ttkbootstrap
from helper.constants import *

from helper import config

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        configuration = config.read()

        w = configuration["width"]
        h = configuration["height"]
        x = int((self.winfo_screenwidth()/2) - (w/2))
        y = int((self.winfo_screenheight()/2) - (h/2))

        self.title("Point of Sales")
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(False, False)
        self.overrideredirect(1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
