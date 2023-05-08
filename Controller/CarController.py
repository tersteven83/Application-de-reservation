from Models.CarModel import CarModel


def trouverid(im):
    """
    Trouver l'id d'un car par son numéro matricul
    :param im: numéro matricul
    :return: id du car
    """
    carmodel = CarModel()
    infocar = carmodel.findBy({"im": im})
    return infocar[0][0]
