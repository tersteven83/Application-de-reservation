import View.voyager as voyager


# import View.liste_passager as liste_passager
# import View.place_dispo as place_dispo

def main():
    print("\t\tCoopérative de Transport Vanilla")
    print("\t\t--------------------------------\n")
    print("\t\tBIENVENU DANS L'APPLICATION DE RÉSERVATION")
    print("\n Quelle action souhaitez-vous faire?")
    menu()


def menu(choix: str = None):
    if choix is None:
        print("1. Réservation(s)")
        print("2. Liste des passagers")
        print("3. Places disponibles")
        print("NB: (q) pour quitter, (**) revenir au menu principal, (*1|*2|*3) revenir au choix précédent")
        choix = input("Entrez votre choix ici: ")

    match choix:
        case '1':
            voyager.reservation()
        case '2':
            voyager.liste_passager()
        case '3':
            voyager.place_disponible()
        case _:
            menu()


if __name__ == '__main__':
    main()
