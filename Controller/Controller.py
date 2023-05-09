def validate(vardict: dict) -> bool:
    """
    Vérifier un variable s'il est vide ou non
    Enlève les indices '_opt' dans les clefs
    :param vardict: dictionnaire de varible à checker
    :return:
    """
    for key, value in vardict.items():
        # si la valeur de clef du dictionnaire n'est pas défini ou vide
        if value is None or value == '':
            # si la clef contient '_opt', on continue la boucle
            if "_opt" in key:
                continue
            # sinon la valeur de la clef n'est pas optionel
            else:
                return False

    return True


def creer_dictionnaire(variables: list) -> dict:
    """
    creer un dictionnaire de variables
    :param variables: noms de variable
    :return:
    """
    dictionary = {}
    for variable in variables:
        # initialiser le contenu du mot pas un vide
        dictionary[variable] = ''

    return dictionary

