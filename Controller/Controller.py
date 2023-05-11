import sys
from typing import Dict, Any

import main
import View.voyager as voyage


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


def creer_dictionnaire(nom_var: list, variables: list = None) -> bool | dict:
    """
    creer un dictionnaire de variables
    :param nom_var: étiquetes des variables
    :param variables: valeurs des variables
    :return:
    """
    if variables is None:
        variables = []

    # si la longueur des deux parametres ne sont pas égaux, on sort et retour faux
    elif len(nom_var) != len(variables):
        return False

    dictionary = {}

    i: int
    for i in range(len(nom_var)):
        # initialiser le contenu du mot pas un vide
        # short hand if
        dictionary[nom_var[i]] = variables[i] if variables[i] else ''

    return dictionary


def value_controller(variable):
    match variable:
        case 'q':
            sys.exit("Opération annulée.")
        case '**':
            main.main()
        case '*1':
            main.menu('1')
        case '*2':
            main.menu('2')
        case '*3':
            main.menu('3')
        case _:
            pass
