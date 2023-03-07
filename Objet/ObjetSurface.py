import Utils.Connexion 
class ObjetSurface:
    
    def __init__(self, idObjet, idRefference, nombre, coordonne):
        self.idObjet = idObjet
        self.idRefference = idRefference
        self.nombre = nombre
        self.coordonne = coordonne
    
    def getById(connexion, id):
        array = []
        notMine = False
        if(connexion == None):
            notMine = True
            connexion = Utils.Connexion.enterBdd()
        cur = connexion.cursor()
        query = "select idObjet, idRefference, nombre, coordonne from objetsurface where idrefference = '"+id+"';"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = ObjetSurface(row[0], row[1], row[2], row[3])
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
        query = "select idObjet, idRefference, nombre, coordonne from objetsurface;"
        cur.execute(query)
        obj_data = cur.fetchall()
        for row in obj_data:
            lalana = ObjetSurface(row[0], row[1], row[2], row[3])
            array.append(lalana)
        cur.close()
        if(notMine):
            connexion.close()
        return array 