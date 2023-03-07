import Utils.Connexion 
class refferenceobjet:
    def __init__(self, idRefference, nom):
        self.idRefference = idRefference
        self.nom = nom
        
    def getAllReffence(connexion):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select idrefference, nom from refferenceobjet";
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            nomroute = refferenceobjet(row[0], row[1])
            array.append(nomroute)
        cur.close()
        if(notMine):
            connexion.close()
        return array