import datetime
import Controller.Controller as Controller

from Models.ClientModel import ClientModel


def estInscrit(tel):
    """
    Vérifier si un client est déja membre
    :param tel: son numéro téléphone
    :return:
    """
    clientmodel = ClientModel()
    client = clientmodel.findBy({"tel": tel})
    if client:
        return True
    else:
        return False


def decrire(tel):
    """
    Décrire un client par biais de son numéro de téléphone
    :param tel:
    :return: id du client après description
    """
    clientmodel = ClientModel()
    client = clientmodel.findBy({"tel": tel})
    nom = client[0][1]
    prenom = client[0][2]
    cin = client[0][3]
    tel = client[0][4]
    sexe = client[0][5]
    inscrit = client[0][6]
    adresse = client[0][7]
    print(f"\tNoms: {nom} {prenom}")
    print(f"\tcin: {cin}")
    print(f"\tNuméro téléphone: {tel}")
    print(f"\tSexe: {sexe}")
    print(f"\tInscrit le: {inscrit}")
    print(f"\tAdresse: {adresse}")
    return client[0][0]


def registre():
    """
    Ajouter un client dans la table client
    :return: id du client créer
    """
    # dictionnaire de variable
    # les contenus du dictionnaire qui a un nom avec '_opt' à la fin peut être null
    info = Controller.creer_dictionnaire(['nom', 'prenom', 'cin_opt', 'tel_opt', 'sexe', 'adresse', 'inscrit'])
    info['nom'] = input("\tNom: ")
    info['prenom'] = input("\tPrénom: ")
    info['cin_opt'] = input("\tNuméro CIN[optionnel]: ")
    info['tel_opt'] = input("\tNuméro télephone[optionnel]: ")
    info['sexe'] = input("\tsexe: ")
    info['adresse'] = input("\tadresse: ")
    info['inscrit'] = datetime.datetime.today()
    if not Controller.validate(info):
        print("----Veuillez bien remplir la formulaire----")
        registre()

    # on crée un client
    clientmodel = ClientModel()
    clientmodel.create({
        'nom': info['nom'],
        'prenom': info['prenom'],
        'cin': info['cin_opt'],
        'tel': info['tel_opt'],
        'sexe': info['sexe'],
        'adresse': info['adresse'],
        'inscrit': info['inscrit']
    })

    clientcreer = clientmodel.findBy({'inscrit': info['inscrit']})
    id_client = clientcreer[0][0]
    return id_client

