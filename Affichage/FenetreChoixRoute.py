from Affichage.PanneauChoix import PanneauChoixBatiment
import tkinter as tk

class FenetreChoixRoute(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(padx=10, pady=50)
        self.title("Road")
        self.geometry("500x200")
        self.panneau = PanneauChoixBatiment(self)
        panneau = self.panneau
        panneau.pack()
        self.mainloop()
    def getPanneau():
        return self.panneau
    def setPanneau(p):
        self.panneau = p
         