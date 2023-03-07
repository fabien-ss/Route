import tkinter as tk
from Objet.dago5 import dago5
from Objet.Materiaux import Materiaux
from Affichage.FenetreLalanaSimba import FenetreLalanaSimba
from Objet.refferenceobjet import refferenceobjet
from Affichage.FenetreResultatRoute import FenetreResultatRoute
from Objet.ObjetSurface import ObjetSurface

class PanneauChoixBatiment(tk.Frame):
    def __init__(self ,parent, master=None):
        tk.Frame.__init__(self, parent)
        nomRoute = refferenceobjet.getAllReffence(None)
        option = []
        for r in nomRoute:
            option.append([r.nom, r.idRefference])
        self.dropdownlist = tk.StringVar()
        self.dropdownlist.set(option[0])
        dropdownlist = tk.OptionMenu(self, self.dropdownlist, *option)
        text = tk.Label(self, text="Critere ")
        text.grid(row=1, column=0)
        dropdownlist.grid(row=1,column=2)
        rl = tk.Label(self, text="Rayon")
        rl.grid(row=2, column=0)
        rayon = tk.Text(self, height= 2, width= 5)
        rayon.insert(tk.END, "0")
        rayon.grid(row=2,column=2)
        self.rayon = rayon
        km = tk.Label(self, text="km")
        km.grid(row=2, column=3)
        recherche = tk.Button(self, text="Recherche", command=self.recherche)
        recherche.grid(row=3, column=2)
        
    def recherche(self):
        valeur = self.dropdownlist.get().replace("(","").replace(")", "").split(",")
        print(valeur[1])
        nomRoute = dago5.getNomderoute(None)
        rayon = int(self.rayon.get("1.0", "end"))
        batiment = ObjetSurface.getById(None, valeur[1])
        nomRouteTrie = dago5.triRoute(batiment, nomRoute, rayon)
        fen = FenetreResultatRoute(nomRouteTrie, valeur[0], rayon)
        #self.destroy()


class PanneauChoixRoute(tk.Frame):
    def __init__(self ,parent, master=None):
        tk.Frame.__init__(self, parent)
        nomRoute = dago5.getNomderoute(None)
        option = nomRoute
        self.dropdownlist = tk.StringVar()
        self.dropdownlist.set(option[0])
        self.LabelFrame = tk.Label(self, text= "Saisir PK de la route a reparer")
        self.button = tk.Button(self, text="Voir sur la carte", command=self.clique)
        dropdownlist = tk.OptionMenu(self, self.dropdownlist, *option)
        dropdownlist.grid(row=0,column=0)
        self.debut = tk.Text(self, height= 2, width= 10)
        debut = self.debut
        debut.insert(tk.END, "Debut")
        debut.grid(row=0, column=1)
        self.fin = tk.Text(self, height= 2, width= 10)
        fin = self.fin
        fin.insert(tk.END, "Fin")
        fin.grid(row=0, column=2)
        button = self.button
        button.grid(row=0,column = 3)
        
    def clique(self):
        materiaux = Materiaux.getMateriaux(None)
        debut = int(self.debut.get("1.0", "end"))
        fin = int(self.fin.get("1.0","end"))
        if(debut > fin):
            raise Exception("debut superieur a fin")
        # ty manome anle izy eh []
        prix = dago5.findEndommagedRoad(self.dropdownlist.get(), debut, fin, materiaux)
        # mampiasa an'ilay
        chaquePoint = dago5.chaquePoint(None, self.dropdownlist.get())
        # coordonnee x kilometrage
        coordsXkilometre = dago5.calcul(chaquePoint)
        # indices des points
        ipkd = dago5.findIndexOfPoints(debut, coordsXkilometre)
        ipka = dago5.findIndexOfPoints(fin, coordsXkilometre)
        # chaque points entre les indicess
        coordonneeDesPoints = dago5.getCoordsBetweenPK(ipkd,ipka, coordsXkilometre)
        # hexadecimale en coordonnee longitude x latitude
        listM = dago5.convertionEnLongitudeEtLatitude(coordonneeDesPoints)
        fen = FenetreLalanaSimba(prix, coordonneeDesPoints, listM)
        
    def getDropdownlist():
        return self.dropdownlist
    def setDropdownlist(s):
        self.dropdownlist = s