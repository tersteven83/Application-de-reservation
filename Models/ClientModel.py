from Model import Model


class ClientModel(Model):
    nom = None
    prenom = None
    cin = None
    tel = None
    sexe = None
    inscrit = None
    adresse = None

    def __init__(self):
        super().__init__()
        self.table = 'client'

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom
        return self

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom
        return self

    def getCin(self):
        return self.cin

    def setCin(self, cin):
        self.cin = cin
        return self

    def getTel(self):
        return self.tel

    def setTel(self, tel):
        self.tel = tel
        return self

    def getSexe(self):
        return self.sexe

    def setSexe(self, sexe):
        self.sexe = sexe
        return self

    def getInscrit(self):
        return self.inscrit

    def setInscrit(self, inscrit):
        self.inscrit = inscrit
        return self

    def getAdresse(self):
        return self.adresse

    def setAdresse(self, adresse):
        self.adresse = adresse
        return self


clientModel = ClientModel()
print(clientModel.findBy({
    "nom": "Blandine",
    "sexe": "F"
}))