from Tkinter import *


class TkinterInterface:
    def __init__(self):
        self.root = Tk()

    def addLabel(self, label):
        l = Label(self.root, text=label)
        l.pack()
        self.root.mainloop()
