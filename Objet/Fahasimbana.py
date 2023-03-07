import Utils.Connexion

class Fahasimbana:
    def __init__(self, id, r, debut, fin, niveau):
        self.idfahasimbana = id
        self.roadno = r
        self.debut = debut
        self.fin = fin
        self.niveau = niveau
    
    def getAllFahasimbana(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select * from lalanasimba where roadno = '"+str(id)+"';"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = Fahasimbana(row[0], row[1], row[2], row[3], row[4])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array
    
    def getFahasimbanaParRoute(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select idfahasimbana, roadno, debut, fin, niveau from lalanasimba where roadno ='"+str(id)+"'"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = Fahasimbana(row[0], row[1], row[2], row[3], row[4])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array
    
    def getFahasimbana(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select * from fahasimbana where idfahasimbana = "+str(id)+" ;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = Fahasimbana(row[0], row[1], row[2], row[3])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array[0]