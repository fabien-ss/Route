import Utils.Connexion 
class Materiaux:
    def __init__(self, idmateriaux, nom, refferece, prix, duree):
        self.idmateriaux = idmateriaux
        self.nom =nom
        self.refference = refferece
        self.prix = prix
        self.duree = duree
    def getMateriauxById(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select idmateriaux,nom, refference, prix,duree from Materiaux;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = Materiaux(row[0], row[1], row[2], row[3], row[4])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array            
    def getMateriaux(connexion):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select idmateriaux,nom, refference, prix,duree from Materiaux;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = Materiaux(row[0], row[1], row[2], row[3], row[4])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array    