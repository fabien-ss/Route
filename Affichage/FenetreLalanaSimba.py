import tkinter as tk
from Affichage.PanneauLalanaSimba import PanneauLalanaSimba 

class FenetreLalanaSimba(tk.Tk):
    def __init__(self, valeurCalculees, tableauCoordonnee, mls, title):
        #tk.Frame.__init__(self, parent)
        super().__init__()
        self.configure(padx=10, pady=40)
        self.title(title)
        self.geometry("800x200")
        self.panneauLalanaSimba = PanneauLalanaSimba(self, valeurCalculees, tableauCoordonnee, mls)
        p = self.panneauLalanaSimba
        p.pack()
        self.mainloop()