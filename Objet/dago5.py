import Utils.Connexion
import Utils.Fonction
from Objet.Fahasimbana import Fahasimbana
from shapely.geometry import LineString, MultiLineString
from sqlalchemy import create_engine
from geoalchemy2 import Geometry
from shapely.wkb import loads
from Objet.Materiaux import Materiaux

#distanciation(pkd, pka, liste)
#calculedistance(ipkd, ipka, liste)
#findindexofpoints(pk, liste)

from Objet.ObjetSurface import ObjetSurface

class dago5:
    
    def lalanaPriorite(rayon, idBatiment):
        batiments = ObjetSurface.getById(None, idBatiment)
        nomderoutes = dago5.getNomderoute(None)
        
    #batiment
    def triRoute(batiment, nomdesroutes, rayon):
        c = Utils.Connexion.enterBdd()
        cur = c.cursor()
        i = 0
        arr = []
        for nr in nomdesroutes:
            compteur = 0
            #alaina daholo ny lalana simba am nr    
            routesSimba = Fahasimbana.getFahasimbanaParRoute(None, nr)
            #chaque coordonnee dans la mls
            chaquePoint = dago5.chaquePoint(None, nr)
            #kilometrise
            coordsXkilometre = dago5.calcul(chaquePoint)
            #print(coordsXkilometre)
            for lalanasimba in routesSimba:  
                ipkd = dago5.findIndexOfPoints(lalanasimba.debut, coordsXkilometre)
                ipka = dago5.findIndexOfPoints(lalanasimba.fin, coordsXkilometre)
                coordonneeDesPK = dago5.getCoordsBetweenPK(ipkd,ipka, coordsXkilometre)
                for k in range(0,len(batiment),1):
                    for i in range(0,len(coordonneeDesPK),1):
                        sql = "Select st_distancesphere('"+coordonneeDesPK[i][0]+"','"+batiment[k].coordonne+"')/1000"
                        cur.execute(sql)
                        result = cur.fetchone()[0]
                        #print(result)
                        #print(str(k)+" saut")
                        if result <= rayon:
                            compteur += 1
                            #print(str(nr) + str(compteur) + " io fa nahita") 
                            #continue
                            break
                            #if(k < len(batiment)-1):  
                                #k += 1
            #tsy tableau io
            #print([nr, compteur])
            if(compteur > len(batiment)):
                compteur = len(batiment)
            arr.append([nr, compteur])
            compteur = 0
        print(arr)
        nomdesroutes = Utils.Fonction.trier(arr, 1) 
        cur.close()
        c.close()
        return nomdesroutes
    
    def convertionEnLongitudeEtLatitude(ll):
        rows = []
        for r in ll:
            rows.append(r)
        geoms = [loads(row[0], hex=True) for row in rows]
        list_point = []
        for i in range(len(geoms)-1):
            list_point.append(LineString([geoms[i], geoms[i+1]]))
        mls = MultiLineString(list_point)
        return mls
    
    def getLalanaAmboarina(ipkd, ipka):
        return None
    def findEndommagedRoad(roadno, pkd, pka,materiaux):
        roads = Fahasimbana.getAllFahasimbana(None, roadno)
        prix = 0
        duree = 0
        lalana = dago5.getLalana(None, roadno)
        for r in roads:
            #materiaux = Materiaux.getMateriaux()
            if r.debut <= pkd and r.fin >= pka:
                fahasimbana = Fahasimbana(1, roadno, pkd, pka, r.niveau)
                prix += dago5.prixDeReviens(fahasimbana, lalana ,materiaux)
                duree += dago5.jourNecessaire(fahasimbana, lalana,materiaux)
            if r.debut > pkd and r.fin < pka:
                fahasimbana = Fahasimbana(1, roadno, r.debut, r.fin, r.niveau)
                prix += dago5.prixDeReviens(fahasimbana, lalana,materiaux)
                duree += dago5.jourNecessaire(fahasimbana, lalana,materiaux)
            if pka <= r.fin and pka > r.debut and pkd < r.debut and pkd < r.fin:
                fahasimbana = Fahasimbana(1, roadno, r.debut, pka, r.niveau)
                prix += dago5.prixDeReviens(fahasimbana, lalana,materiaux)
                duree += dago5.jourNecessaire(fahasimbana, lalana,materiaux)
            if r.debut <= pkd and r.fin > pkd and r.debut < pka and r.fin < pka:
                fahasimbana = Fahasimbana(1, roadno, pkd, r.fin, r.niveau)
                prix += dago5.prixDeReviens(fahasimbana, lalana,materiaux)
                duree += dago5.jourNecessaire(fahasimbana, lalana,materiaux)
        return [prix, duree]
                         
  
    def prixTotal(materiaux, surface, lalana):
        prix = 0
        for m in materiaux:
            if(int(lalana[0].surftype)==m.idmateriaux):
                prix += m.prix * surface
        return prix
    
    def jourTotal(materiaux, surface, lalana):
        prix = 0
        for m in materiaux:
            if(int(lalana[0].surftype)==m.idmateriaux):
                prix += surface/m.duree
        return prix
    
    def jourNecessaire(fahasimbana, lalana, materiaux):
        longueur = fahasimbana.fin-fahasimbana.debut 
        surface = (longueur*1000) * (lalana[0].width) * (fahasimbana.niveau/10)
        return dago5.jourTotal(materiaux, surface, lalana)
    
    def prixDeReviens(fahasimbana, lalana, materiaux):
        longueur = fahasimbana.fin-fahasimbana.debut 
        surface = (longueur*1000) * (lalana[0].width) * (fahasimbana.niveau/10)
        return dago5.prixTotal(materiaux, surface, lalana)
    
    def distanciation(pkd, pka, liste):
        ipkd = dago5.findIndexOfPoints(pkd, liste)
        ipka = dago5.findIndexOfPoints(pka, liste)
        longeur = dago5.calculeDistance(ipkd, ipka, liste)
        return longeur
    
    def getCoordsBetweenPK(iPKD, iPKA, coords):
        connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        _coords = []
        for i in range(iPKD, iPKA+1):
            _coords.append(coords[i])
        cur.close()
        connexion.close()
        return _coords
    
    def calculeDistance(iPKD, iPKA, coordonnes):
        coords = []
        for i in range(iPKD, iPKA+1):
            coords.append(coordonnes[i])
        return coords
    
    def findIndexOfPoints(pk, liste):
        i = 0
        while(pk > liste[i][1]):
            i += 1
        return i                
    
    def getLongueur(Connexion ,id):
        lalana = dago5.chaquePoint(Connexion,id)
        dist = dago5.calcul(lalana)
        return dist
    
    def somme(mls):
        total_length = 0.0
        for line in mls:
            coords = list(line.coords)
            line_string = LineString(coords)
            length = line_string.length
            total_length += length
        return total_length
    
    def calcul(lalana):
        array = []
        c = Utils.Connexion.enterBdd()
        cur = c.cursor()
        distance = 0
        v = 0;
        for i in range(0,len(lalana),1):
            array.append([lalana[i].geom, distance])
            if(i != len(lalana)-1):
                debut = lalana[i].geom
                fin = lalana[i+1].geom
                if(debut != fin):
                    req = "SELECT ST_DistanceSPHERE("+"'"+str(debut)+"'"+","+"'"+str(fin)+"'"+")/1000;"
                    cur.execute(req)
                    result = cur.fetchone()[0]
                    distance += result
        c.close()
        return array
    
    def getNomderoute(connexion):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select roadno from dago5 group by roadno";
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            nomroute = row[0]
            array.append(nomroute)
        cur.close()
        if(notMine):
            connexion.close()
        return array
    
    def chaquePoint(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select gid, roadno, start_km, end_km, lengthkm, width, (st_dumpPoints(geom)).geom, profondeur,surftype from dago5 where roadno = '"+str(id)+"' order by start_km;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = dago5(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            array.append(lalana)
        if(notMine):
            connexion.close()
        return array    
    
    def getAllGroup(connexion):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select gid, roadno, start_km, end_km, lengthkm, width, geom, profondeur, surftype from dago5 group by roadno;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = dago5(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array 
    
    def getAll(connexion):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select gid, roadno, start_km, end_km, lengthkm, width, geom, profondeur, surftype from dago5;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = dago5(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array    
    
    
    def getLalana(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select gid, roadno, start_km, end_km, lengthkm, width, geom, profondeur, surftype from dago5 where roadno = '"+str(id)+"';"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = dago5(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array    
    
    def __init__(self, gid, roadno, start_km, end_km, lengthkm, width, geom, profondeur, surftype):
        self.gid = gid
        self.roadno = roadno
        self.start_km = start_km
        self.end_km = end_km
        self.lengthkm = lengthkm
        self.width = width
        self.geom = geom
        self.profondeur = profondeur
        self.nombreDeBatimentAlentour = 0
        self.surftype = surftype
    
    def setSurftype(s):
        dago5.surftype = s
    def geSurftype():
        return dago5.surftype
    def setGid(git):
        dago5.gid = git
    def geGid():
        return dago5.gid
    def setRoadno(r):
        dago5.roadno = r
    def getRoadno():
        return dago5.roadno
    def setStart_Km(s):
        dago5.start_km = s
    def getStart_Km(s):
        return dago5.start_km
    def setEnd_Km(s):
        dago5.end_km = s
    def getEnd_Km(s):
        return dago5.end_km
    def getWidth():
        return dago5.width
    def setWidth(s):
        dago5.width = s
    def setGeom(s):
        dago5.geom = s
    def getGeom():
        return dago5.geom