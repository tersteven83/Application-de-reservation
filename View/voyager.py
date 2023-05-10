import datetime
import Controller.VoyagerController as Voyage
import Controller.ClientController as Client
import Controller.CarController as Car
import re


def reservation():
    global im, num_place
    place = []
    # id des voyageurs
    id_client = []
    dest = ''
    date_reserv = ''
    id_car = None
    # on récupère la destination et on l'envoi à place_dispo
    # les destinations possibles sont
    dest_possible = dict(f="Fianarantsoa", t="Tamatave", m="Majunga", mo="Moramanga")
    while dest not in dest_possible:
        dest = input("Destination: (F)ianarantsoa, (M)ajunga, (T)amatave, (Mo)ramanga: ").lower()

    # date de reservation
    date_format = re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$')
    heure_format = re.compile(r'^\d{2}:\d{2}')
    while not date_format.match(date_reserv) and not heure_format.match(date_reserv):
        date_reserv = input("Date de voyage(dd/mm/yyyy hh:mm ou hh:mm(si aujourd'hui)): ")

    # on affiche les places disponibles
    if date_format.match(date_reserv):
        date_reserv = datetime.datetime.strptime(date_reserv, "%d/%m/%Y %H:%M")
        # info dispo est un tuple qui contient deux valeurs, id_car et place_dispo
        info_dispo = Voyage.placedispo(dest_possible[dest], date_reserv)

    else:
        # data d'aujourd'hui avec heure
        date_reserv = str(datetime.date.today()) + " " + date_reserv
        date_reserv = datetime.datetime.strptime(date_reserv, "%Y-%m-%d %H:%M")
        info_dispo = Voyage.placedispo(dest_possible[dest], date_reserv)

    # on récupère l'id_car dans l'index 0 de info_dispo
    if info_dispo:
        id_car = info_dispo[0]
        place_dispo = info_dispo[1]

    # raha vo mamerina none le methode etsy ambony de manonatany oe firy ny num anle fiara andehanana
    if id_car is None:
        trouver = False
        while not trouver:
            im = input("Entrez le numéro matricule du véhicule: ")
            # si l'id de vehicule n'est pas None, on sort de la boucle
            if Car.trouverid(im):
                trouver = True
        id_car = Car.trouverid(im)

    # récupérer le numéro téléphone du client
    # si le num existe déja... on affiche sa description
    # sinon rempli un formulaire
    tel = input("Numéro téléphone du client: ")
    if Client.estInscrit(tel):
        # rehefa avy manao description de averina kely ny id anle olona
        id_client.append(Client.decrire(tel))
    else:
        # rehefa avy manao registre de averina kely ny id anle olona
        id_client.append(Client.registre())

    # recuperer le nombre de bagage
    nb_bagage = int(input("Nombre de bagage: "))

    # récuperer le nombre de place commander par le client
    nb_place = int(input("Nombre de place: "))

    # récuperer le numéro de la place
    for i in range(nb_place):
        if i > 0:
            id_client.append(Client.registre())
        # vérifié si la placee est déjà prise
        # si oui on boucle, et on notif
        verifie = False
        while not verifie:
            num_place = input("Place numéro: ")
            if num_place in place_dispo:
                break
            else:
                print("---Les places libres sont {}---".format(", ".join(place_dispo)))
                print("Veuillez vérifier votre saisi.")
        place.append(num_place)

    # ajouter le Voyage dans le cahier de registre
    Voyage.registre(id_client, id_car, dest_possible[dest], date_reserv, place, nb_bagage)
