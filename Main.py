from Affichage.FenetreChoixRoute import FenetreChoixRoute
import Utils.Connexion 
#from Objet import dago5
#import xml.etree.ElementTree as ET
# from Fahasimbana import Fahasimbana
# from FenetreCarte import MainWindow
    
# lalana = dago5.chaquePoint(None, "RNP 7")
# lalana2 = dago5.calcul(lalana)
# lon = dago5.distanciation(45, 100, lalana2)
# print(lon)

# o = dago5.getLongueur(None, "RNP 7")

# for l in o:
#     print(l)

#45.16 / 100.97


# f = Fahasimbana(2, 'RNP 2', 20, 21, 40)
# pr = dago5.jourNecessaire(f)
# print(pr)
# coords = dago5.chaquePoint(None, 'RNP 2')
# dist = dago5.calcul(coords)

# iPKD = dago5.findIndexOfPoints(20, dist)
# iPKA = dago5.findIndexOfPoints(25, dist)
# _coords = dago5.getCoordsBetweenPK(iPKD, iPKA, dist)
# print(_coords)

# mls = dago5.get_multilinestrings_from_postgresql("localhost", 5432, "bddspaciale","fabien","fabien","dago5", "geom")
# for l  in mls:
#     print(l)
# s = dago5.somme(mls)
# print(s)

fenetre = FenetreChoixRoute()
# ind = 3
# print("Je suis %s", ind)
d = Utils.Connexion.enterBdd()
print(d)