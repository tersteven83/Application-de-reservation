from Model import Model


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
