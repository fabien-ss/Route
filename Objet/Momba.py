import tkinter as tk
from Objet.dago5 import dago5

class Momba(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        nomRoute = dago5.getNomderoute(None)
        option = nomRoute
        self.dropdownlist = tk.StringVar()
        self.dropdownlist.set(option[0])
        self.button = tk.Button(self, text="ok", command=self.clique)
        dropdownlist = tk.OptionMenu(self, self.dropdownlist, *option)
        dropdownlist.pack()
        button = self.button
        button.pack()
        
    def clique(self):
        print(self.dropdownlist.get())
    def getDropdownlist():
        return self.dropdownlist
    def setDropdownlist(s):
        self.dropdownlist = s
    