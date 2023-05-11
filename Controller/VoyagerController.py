import re
import datetime

import Controller.Controller as Controller
from Models.VoyagerModel import VoyagerModel
from Models.CarModel import CarModel


def placedispo(dest, depart: datetime):
    """
    Cette fonction la liste des places disponibles dans un véhicule
    :param dest: lieu de destination
    :param depart: date de départ
    :return: id du véhicule dans la base de donnée et les places disponibles
    """
    voyage = VoyagerModel()
    liste_voyageur = voyage.findBy({
        "destination": dest,
        "date_heure": str(depart)
    })
    # rehefa vide le liste
    if not liste_voyageur:
        return None
    id_car = liste_voyageur[0][2]

    # on récupère le nombre de places d'une voiture
    carmodel = CarModel()
    infocar = carmodel.find(id_car)  # retourner liste
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
    print(f"Place(s) libre(s): {affiche_placelibre}")

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


def destination(possibilite: dict) -> str:
    """
    Demande à l'utilisateur sa destination jusqu'à ce que son entrée au clavier soit dans le dictionnaire
    :param possibilite: dictionnaire comme {"m": "Mahajanga", "t": "Toamasina"....}
    :return:
    """
    dest = ''
    choix_possible = []
    for key, value in possibilite.items():
        choix_possible.append("({}){}".format(key.upper(), value[len(key):]))
    # on converti les choix possibles en chaines de caractères
    choix_possible = ', '.join(choix_possible)

    while dest not in possibilite:
        dest = input("Destination: {}: ".format(choix_possible)).lower()
        Controller.value_controller(dest)

    return dest


def date_reservation() -> datetime:
    """
    Récupérer la date de réservation
    :return: date de réservation
    """
    date_reserv = ''
    # format de la date
    date_format = re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$')
    heure_format = re.compile(r'^\d{2}:\d{2}')
    while not date_format.match(date_reserv) and not heure_format.match(date_reserv):
        date_reserv = input("Date de voyage(dd/mm/yyyy hh:mm ou hh:mm(si aujourd'hui)): ")
        Controller.value_controller(date_reserv)

    if date_format.match(date_reserv):
        date_reserv = datetime.datetime.strptime(date_reserv, "%d/%m/%Y %H:%M")

    else:
        # data d'aujourd'hui avec heure
        date_reserv = "{0} {1}".format(str(datetime.date.today()), date_reserv)
        date_reserv = datetime.datetime.strptime(date_reserv, "%Y-%m-%d %H:%M")

    return date_reserv


def liste_passager(dest, depart: datetime) -> dict:
    """
    Récupérer la liste des passagers
    :param dest: destination
    :param depart: date de depart
    :return:
    """
    voyageurs = {
        "Place": [],
        "Noms": [],
        "CIN": [],
        "Sexe": [],
        "Destination": []
    }
    place = voyageurs['Place']
    nom = voyageurs['Noms']
    dests = voyageurs['Destination']
    sexe = voyageurs['Sexe']
    cin = voyageurs['CIN']
    voyagermodel = VoyagerModel()
    liste = voyagermodel.liste_passager(dest, depart)

    for champ in liste:
        place.append(champ[0])
        nom.append(champ[1])
        sexe.append(champ[2])
        cin.append(champ[3])
        dests.append(champ[4])

    return voyageurs


def supprimer_de_liste(criteres: dict):
    """
    supprimer une ligne de la liste des passagers
    :param criteres:
    :return:
    """
    voyagermodel = VoyagerModel()
    voyagermodel.supprimer(criteres)
