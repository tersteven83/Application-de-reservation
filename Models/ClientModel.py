from Models.Model import Model


class ClientModel(Model):
    __id = None
    __nom = None
    __prenom = None
    __cin = None
    __tel = None
    __sexe = None
    __inscrit = None
    __adresse = None

    def __init__(self):
        super().__init__()
        self._table = 'client'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def cin(self):
        return self.__cin

    @cin.setter
    def cin(self, cin):
        self.__cin = cin

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self, sexe):
        self.__sexe = sexe

    @property
    def inscrit(self):
        return self.__inscrit

    @inscrit.setter
    def inscrit(self, inscrit):
        self.__inscrit = inscrit

    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse

