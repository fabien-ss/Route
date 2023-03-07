from Affichage.FenetreLalanaSimba import FenetreLalanaSimba
from Objet.Materiaux import Materiaux
from Objet.dago5 import dago5
import tkinter as tk
from tkinter import ttk

class PanneauListeRoute(tk.Frame):
    def __init__(self, parent, listeroute):
        tk.Frame.__init__(self, parent)
        #nomRoute = dago5.getNomderoute(None)
        tree = ttk.Treeview(self, columns=('ROUTE', 'nombre'))
        tree.heading("ROUTE", text="Route")
        tree.heading("nombre", text="Nombre")
        for r in listeroute:
            tree.insert('', 'end', text=r[0], values=(r[0], r[1]))
        tree.grid(row=0, column=0)
        self.tree = tree
        self.debut = tk.Text(self, height= 2, width= 10)
        debut = self.debut
        debut.insert(tk.END, "0")
        
        lab2 = tk.Label(self, text="PK Debut")
        lab2.grid(row=0, column=1)
        
        debut.grid(row=0, column=2)
        self.fin = tk.Text(self, height= 2, width= 10)
        fin = self.fin
        
        lab = tk.Label(self, text="PK FIN")
        lab.grid(row=0, column=3)
        
        fin.insert(tk.END, "100")
        fin.grid(row=0, column=4)
        recherche = tk.Button(self, text="Resultat", command=self.clique)
        recherche.grid(row=1, column=2)
        
    def clique(self):
        selected = self.tree.item(self.tree.selection())['text'] 
        materiaux = Materiaux.getMateriaux(None)
        debut = int(self.debut.get("1.0", "end"))
        fin = int(self.fin.get("1.0","end"))
        if(debut > fin):
            raise Exception("debut superieur a fin")
        prix = dago5.findEndommagedRoad(selected, debut, fin, materiaux)
        chaquePoint = dago5.chaquePoint(None, selected)
        coordsXkilometre = dago5.calcul(chaquePoint)
        ipkd = dago5.findIndexOfPoints(debut, coordsXkilometre)
        ipka = dago5.findIndexOfPoints(fin, coordsXkilometre)
        coordonneeDesPoints = dago5.getCoordsBetweenPK(ipkd,ipka, coordsXkilometre)
        listM = dago5.convertionEnLongitudeEtLatitude(coordonneeDesPoints)
        fen = FenetreLalanaSimba(prix, coordonneeDesPoints, listM, selected)