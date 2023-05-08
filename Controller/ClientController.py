from Models.ClientModel import ClientModel


def estInscrit(tel):
    """
    Vérifier si un client est déja membre
    :param tel: son numéro téléphone
    :return:
    """
    clientmodel = ClientModel()
    client = clientmodel.findBy({"tel": tel})
    if client is not None:
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
    print(f"Nom: {nom}")
    print(f"prenom: {prenom}")
    print(f"cin: {cin}")
    print(f"tel: {tel}")
    print(f"sexe: {sexe}")
    print(f"inscrit: {inscrit}")
    print(f"adresse: {adresse}")
    return client[0][0]


def registre():
    """
    Ajouter un client dans la table client
    :return:
    """
    input("Nom: ")
    input("prenom: ")
    input("cin: ")
    input("tel: ")
    input("sexe: ")
    input("adresse: ")
