from Models.CarModel import CarModel
import Controller.Controller as Controller


def trouverid(im):
    """
    Trouver l'id d'un car par son numéro matricul
    :param im: numéro matricul
    :return: id du car
    """
    carmodel = CarModel()
    infocar = carmodel.findBy({"im": im})
    if not infocar:
        return False
    return infocar[0][0]


def info_car(identifier: int) -> dict:
    carmodel = CarModel()
    info = carmodel.find(identifier)
    info = Controller.creer_dictionnaire(['id', 'marque', 'model', 'im', 'chauff', 'nb_place', 'nb_voyage'],
                                         info)
    return info