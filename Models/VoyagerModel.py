import datetime

from Models.Model import Model


class VoyagerModel(Model):
    __id = None
    __id_client = None
    __id_car = None
    __destination = None
    __date_heure = None
    __num_place = None
    __nb_bagage = None
    __lieudemb = None

    def __init__(self):
        super().__init__()
        self._table = 'voyager'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def id_client(self):
        return self.__id_client

    @id_client.setter
    def id_client(self, id_client):
        self.__id_client = id_client

    @property
    def id_car(self):
        return self.__id_car

    @id_car.setter
    def id_car(self, id_car):
        self.__id_car = id_car

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def date_heure(self):
        return self.__date_heure

    @date_heure.setter
    def date_heure(self, date_heure):
        self.__date_heure = date_heure

    @property
    def num_place(self):
        return self.__num_place

    @num_place.setter
    def num_place(self, num_place):
        self.__num_place = num_place

    @property
    def nb_bagage(self):
        return self.__nb_bagage

    @nb_bagage.setter
    def nb_bagage(self, nb_bagage):
        self.__nb_bagage = nb_bagage

    @property
    def lieudemb(self):
        return self.__lieudemb

    @lieudemb.setter
    def lieudemb(self, lieudemb):
        self.__lieudemb = lieudemb

    def liste_passager(self, dest, depart: datetime):
        return self.requete(f"SELECT voyager.num_place AS Place, concat(nom, ' ', prenom) AS Noms, sexe, cin,  destination FROM client\
        INNER JOIN {self._table} ON client.id=voyager.id_client \
        WHERE date_heure='{depart}' AND destination='{dest}' ORDER BY Place").fetchall()

    def supprimer(self, criteres: dict):
        liste_des_cols = []  # ce liste de col doit etre de la forme col1=%s AND col2=%s....
        liste_des_vals = []
        for key, value in criteres.items():
            liste_des_cols.append(key + '=%s')  # dans la boucle, c'est encore de la forme de liste
            liste_des_vals.append(value)
        # on doit merge la liste en string par le séparateur 'AND'
        cols = " AND ".join(liste_des_cols)

        return self.requete(f"DELETE FROM {self._table} WHERE {cols}", liste_des_vals, True)

    def findByDate(self, depart: datetime, identifier: int = None):
        """
        Trouver un voyage par date
        :param identifier: id d'un véhicule
        :param depart: date de réservation|départ
        :return:
        """
        if type(depart) == datetime.datetime:
            depart = depart.date()
        if identifier is None:
            return self.requete(f"SELECT * FROM {self._table} WHERE date_trunc('day', date_heure)='{depart}'").fetchall()
        else:
            return self.requete(f"SELECT * FROM {self._table} WHERE date_trunc('day', date_heure)='{depart}' AND id_car={identifier}").fetchall()
