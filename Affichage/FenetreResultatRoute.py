from Affichage.PanneauListeRoute import PanneauListeRoute# import PanneauListeRoute
import tkinter as tk

class FenetreResultatRoute(tk.Tk):
    def __init__(self, route, titre, rayon):
        super().__init__()
        self.title("Resultat recherche pour "+str(titre)+" sur un rayon de "+str(rayon)+" km")
        self.configure(padx=10, pady=40)
        self.geometry("1000x350")
        self.panneau = PanneauListeRoute(self, route)
        panneau = self.panneau
        panneau.pack()
        self.mainloop()
    def getPanneau():
        return self.panneau
    def setPanneau(p):
        self.panneau = p