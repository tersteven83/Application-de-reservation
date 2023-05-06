from Model import Model


class CarModel(Model):
    __id = None
    __marque = None
    __model = None
    __im = None
    __nom_chauff = None
    __nb_place = None
    __nb_voyage = None

    def __init__(self):
        super().__init__()
        self._table = 'car'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, marque):
        self.__marque = marque

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def im(self):
        return self.__im

    @im.setter
    def im(self, im):
        self.__im = im

    @property
    def nom_chauff(self):
        return self.__nom_chauff

    @nom_chauff.setter
    def nom_chauff(self, nom_chauff):
        self.__nom_chauff = nom_chauff

    @property
    def nb_place(self):
        return self.__nb_place

    @nb_place.setter
    def nb_place(self, nb_place):
        self.__nb_place = nb_place

    @property
    def nb_voyage(self):
        return self.__nb_voyage

    @nb_voyage.setter
    def nb_voyage(self, nb_voyage):
        self.__nb_voyage = nb_voyage


carModel = CarModel()
# carModel.create({
#     "marque": "Sprinter",
#     "model": "412",
#     "im": "2314TAB",
#     "nom_chauff": "RABE",
#     "nb_place": 12,
#     "nb_voyage": 1
# })

print(carModel.findAll())
