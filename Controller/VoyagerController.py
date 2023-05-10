from datetime import datetime

from Models.VoyagerModel import VoyagerModel
from Models.CarModel import CarModel


def placedispo(destination, depart: datetime):
    """
    Cette fonction la liste des places disponibles dans un véhicule
    :param destination: lieu de destination
    :param depart: date de départ
    :return: id du véhicule dans la base de donnée
    """
    voyage = VoyagerModel()
    liste_voyageur = voyage.findBy({
        "destination": destination,
        "date_heure": str(depart)
    })
    # rehefa vide le liste
    if not liste_voyageur:
        return None
    id_car = liste_voyageur[0][2]

    # on récupère le nombre de places d'une voiture
    carmodel = CarModel()
    infocar = carmodel.find(id_car) # retourner liste
    nb_place = infocar[5]  # la colonne nb_place de la table 'car' se trouve à l'index 5

    # on liste les places disponibles
    # louper jusq le dernier nb de place,
    # louper à travers la liste des voyageurs
    placelibre = []
    for num_place in range(1, nb_place + 1):
        sortir = False
        for voyageur in liste_voyageur:
            if voyageur[5] == num_place:  # la colonne num_place de la table 'voyager' se trouve à l'index 5
                # la place num_place est déjà prise
                # on break out de la boucle des voyageurs
                # on continu la boucle pour le num_place
                sortir = True
                break
        if sortir:
            continue
        placelibre.append(f"{num_place}")

    # on affiche les places libres
    # on convertit la liste de place libre en string
    affiche_placelibre = ' ,'.join(placelibre)
    print(f"Les places libres sont: {affiche_placelibre}")

    # on retourne l'id_car
    return id_car, placelibre


def registre(id_client, id_car, dest, date_reserv, place, nb_bagage):
    """
    Ajout des voyageurs dans la table 'voyager'
    :param id_client: list des id clients
    :param id_car:
    :param dest: la destination du voyageur
    :param date_reserv: la date de réservation
    :param place: list place occupé
    :param nb_bagage:
    :return:
    """
    voyagermodel = VoyagerModel()
    for i in range(len(id_client)):
        voyagermodel.create({
            "id_client": id_client[i],
            "id_car": id_car,
            "destination": dest,
            "date_heure": date_reserv,
            "num_place": place[i],
            "nb_bagage": nb_bagage
        })
