# import Controller.VoyagerController as Voyage
import Controller.VoyagerController as Voyage
import Controller.ClientController as Client
import Controller.CarController as Car
import Controller.Controller as Controller
from prettytable import PrettyTable
import re

import main


def reservation():
    global im, num_place
    place = []
    # id des voyageurs
    id_client = []
    dest = ''
    id_car = None
    place_dispo = []

    print("\t\t\t-----RESERVATION-----")

    # on récupère la destination et on l'envoi à place_dispo
    # les destinations possibles sont
    dest_possible = dict(f="Fianarantsoa", t="Tamatave", m="Majunga", mo="Moramanga")
    dest = Voyage.destination(dest_possible)

    # date de reservation
    date_reserv = Voyage.date_reservation(True)

    # on affiche les places disponibles
    # info dispo est un tuple qui contient deux valeurs, id_car et place_dispo
    info_dispo = Voyage.placedispo(dest_possible[dest], date_reserv)
    # on récupère l'id_car dans l'index 0 de info_dispo
    if info_dispo:
        id_car = info_dispo[0]
        place_dispo = info_dispo[1]

    # raha vo mamerina none le methode etsy ambony de manonatany oe firy ny num anle fiara andehanana
    # la valeur initial de id_car n'est pas changé par la méthode ci-dessus
    if id_car is None:
        trouver = False
        while not trouver:
            print(f"\t\tINITIATION DU VOYAGE du {date_reserv}")
            im = input("Entrez le numéro matricule du véhicule: ")
            Controller.value_controller(im)
            # si l'id de vehicule n'est pas None, on sort de la boucle
            if Car.trouverid(im):
                trouver = True
        id_car = Car.trouverid(im)

    # récupérer le numéro téléphone du client
    # si le num existe déja... on affiche sa description
    # sinon rempli un formulaire
    tel = input("Numéro téléphone du client: ")
    Controller.value_controller(tel)
    if Client.estInscrit(tel):
        # rehefa avy manao description de averina kely ny id anle olona
        id_client.append(Client.decrire(tel))
    else:
        # rehefa avy manao registre de averina kely ny id anle olona
        print("\t\t-----Ce client n'existe pas encore, veuillez l'enregistrer-----")
        id_client.append(Client.registre())

    # recuperer le nombre de bagage
    nb_bagage = int(input("Nombre de bagage: "))

    # récuperer le nombre de place commander par le client
    nb_place = int(input("Nombre de place: "))

    # récuperer le numéro de la place
    for i in range(nb_place):
        if i > 0:
            # si la place est plus grande que 0, càd le client demande d'autres places à part la sienne,
            # on demande alors les infos de ses compagnons
            print("\t\t-----Veuillez renseigner les companies du client-----")
            id_client.append(Client.registre())

        # vérifié si la placee est déjà prise
        # si oui on boucle, et on notif
        verifie = False
        while not verifie:
            num_place = input("Place numéro: ")
            Controller.value_controller(num_place)

            # si le num_place saisi est parmis les places dispo
            if num_place in place_dispo:
                # supprimer le num_place du place_dispo
                place_dispo.pop(place_dispo.index(num_place))
                break
            elif len(place_dispo) == 0:
                break
            else:
                print("---Les places libres sont {}---".format(", ".join(place_dispo)))
                print("Veuillez vérifier votre saisi.")
        place.append(num_place)

    # ajouter le Voyage dans le cahier de registre
    Voyage.registre(id_client, id_car, dest_possible[dest], date_reserv, place, nb_bagage)
    print("\t\t\t~~~~~~Opération effectué~~~~~~")
    action = input(
        "q:quitter;\t **:Revenir au menu principal;\t *1|*2|*3: Réservation|Liste des passagers|Places disponibles:  ")
    Controller.value_controller(action)


def liste_passager(formulaire=True, destnat=None, depart=None):
    global info_car, place
    id_car = None
    place_dispo = []
    action = ''

    print("\t\t\t-----LISTE DES PASSAGERS-----")

    # on récupère la destination et on l'envoi à place_dispo
    # les destinations possibles sont
    dest_possible = dict(f="Fianarantsoa", t="Tamatave", m="Majunga", mo="Moramanga")
    # si on éxige un formulaire
    if formulaire:
        dest = Voyage.destination(dest_possible)
        # récupérer la date de réservation
        date_reserv = Voyage.date_reservation()

    else:
        # on n'exige pas de formulaire
        dest = destnat
        date_reserv = depart

    voyageurs = Voyage.liste_passager(dest_possible[dest], date_reserv)
    draw_table(voyageurs)

    # info du véhicule
    # récuperer l'id de la voiture et sa place disponible du voyage
    info_dispo = Voyage.placedispo(dest_possible[dest], date_reserv)
    if info_dispo:
        id_car = info_dispo[0]
        place_dispo = info_dispo[1]
        info_car = Car.info_car(id_car)
        print(
            f"Chauffeur: {info_car['chauff']}\t\t\tNuméro d'immatriculation: {info_car['im']} \t\t\t Marque: {info_car['marque']} {info_car['model']}"
            f"\t\t{info_car['nb_place']} places")

    print("\nQuelle action souhaitez-vous faire?")
    verifier = False
    while not verifier:
        action = input("(R)éservation; (S)upprimer: ").lower()
        Controller.value_controller(action)
        if action in ['r', 's']:
            verifier = True

    # choix des actions faites par l'utilisateur
    if action == 'r':
        main.menu('1')
    else:
        # suppression
        # demander le numéro de place du client
        verifier = False
        while not verifier:
            place = int(input("Place numéro: "))
            # si le num place est parmi les déjà occupés et n'est pas supérieur aux nombres de places du véhicule
            if place not in place_dispo and place <= info_car['nb_place']:
                verifier = True
            else:
                print("****Vérifier votre saisi, consulter la liste des passagers****")

        Voyage.supprimer_de_liste({'num_place': place, 'date_heure': date_reserv})
        liste_passager(formulaire=False, destnat=dest, depart=date_reserv)


def draw_table(dictionnaire: dict):
    """
    Dessiner un tableau
    :param dictionnaire: dictionnaire par item et construit par colone
    :return:
    """
    # create a new table
    table = PrettyTable()

    for key, value in dictionnaire.items():
        table.add_column(key, value)

    # set the table style
    table.border = True
    table.header_style = "title"
    table.align = "l"

    # print the table
    print(table)


def place_disponible():
    print("\t\t\t-----PLACES DISPONIBLES-----")

    # on récupère la destination et on l'envoi à place_dispo
    # les destinations possibles sont
    dest_possible = dict(f="Fianarantsoa", t="Tamatave", m="Majunga", mo="Moramanga")

    dest = Voyage.destination(dest_possible)
    # récupérer la date de réservation
    date_reserv = Voyage.date_reservation()

    # info du véhicule
    # récuperer l'id de la voiture et sa place disponible du voyage
    info_dispo = Voyage.placedispo(dest_possible[dest], date_reserv)
    if info_dispo:
        id_car = info_dispo[0]
        place_dispo = info_dispo[1]
        info_car = Car.info_car(id_car)

        # dessiner l'interieur de la voiture
        dessiner_voiture(info_car['nb_place'], place_dispo)

        print(
            f"Chauffeur: {info_car['chauff']}\t\t\tNuméro d'immatriculation: {info_car['im']} \t\t\t Marque: {info_car['marque']} {info_car['model']}"
            f"\t\t{info_car['nb_place']} places")

        action = input(
            "q:quitter;\t **:Revenir au menu principal;\t *1|*2|*3: Réservation|Liste des passagers|Places disponibles:  ")
        Controller.value_controller(action)


def dessiner_voiture(nb_place, place_dispo):
    table = PrettyTable()
    # determiner le nombre de rangé du véhicule
    nb_range = int(nb_place / 3)
    j = 1
    for i in range(1, nb_range):
        # regler le pas de l'incrementation par rangé de j
        if i == 1:
            rang = [" ", " ", j, j + 1]
            rang = verifier_siege(rang, place_dispo)
            table.add_row(rang)
            j += 2
        if i == 1 or i == nb_range-1:
            rang = [j for j in range(j, j + 4)]
            rang = verifier_siege(rang, place_dispo)
            table.add_row(rang)
            j += 4
        else:
            rang = [j, j+1, " ", j+2]
            rang = verifier_siege(rang, place_dispo)
            table.add_row(rang)
            j += 3

    table.align = 'c'
    table.border = True
    table.header = False
    print(table)


def verifier_siege(sieges: list, place_dispo: list) -> list:
    """
    Vérifier si la siège est prise ou non, si elle est prise, on supprime la siege
    :param place_dispo:
    :param sieges:
    :return: liste des sieges libres
    """
    for i in range(len(sieges)):
        # si le siege est parmis les places disponibles, on continue, sinon on l'efface
        if str(sieges[i]) in place_dispo:
            continue
        sieges[i] = ' '

    return sieges
