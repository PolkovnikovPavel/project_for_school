import tkinter
from PIL import Image, ImageTk


class Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tkinter.BOTH, expand=1)

        load = Image.open("blast.png")
        render = ImageTk.PhotoImage(load)
        self.img = tkinter.Label(self, image=render)
        self.img.image = render
        self.img.place(x=50, y=200)
