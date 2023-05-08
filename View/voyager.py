import datetime
import Controller.VoyagerController as Voyage
import Controller.ClientController as Client
import Controller.CarController as Car
import re


def reservation():
    place = []
    # id des voyageurs
    id_client = []
    dest = ''
    date_reserv = ''
    # on récupère la destination et on l'envoi à place_dispo
    # les destinations possibles sont
    dest_possible = dict(f="Fianarantsoa", t="Tamatave", m="Majunga", mo="Moramanga")
    while dest not in dest_possible:
        dest = input("Destination: (F)ianarantsoa, (M)ajunga, (T)amatave, (Mo)ramanga: ").lower()

    # date de reservation
    date_format = re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$')
    heure_format = re.compile(r'^\d{2}:\d{2}')
    while not date_format.match(date_reserv):
        date_reserv = input("Date de voyage(dd/mm/yyyy hh:mm ou hh:mm(si aujourd'hui)): ")

    # on affiche les places disponibles
    if date_format.match(date_reserv):
        id_car = Voyage.placedispo(dest_possible[dest], datetime.datetime.strptime(date_reserv, "%Y-%m-%d %H:%M"))
    else:
        id_car = Voyage.placedispo(dest_possible[dest], str(datetime.datetime.today()) + date_reserv)

    # raha vo mamerina none le methode etsy ambony de manonatany oe firy ny num anle fiara andehanana
    if id_car is None:
        trouver = False
        while not trouver:
            im = input("Entrez le numéro matricule du véhicule: ")
            id_car = Car.trouverid(im)
            # si l'id de vehicule n'est pas None, on sort de la boucle
            if id_car:
                trouver = True

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
        if i > 1:
            id_client.append(Client.registre())
        place.append(int(input("Place numéro: ")))

    # ajouter le Voyage dans le cahier de registre
    Voyage.registre(id_client, id_car, dest_possible[dest], date_reserv, place, nb_bagage)
