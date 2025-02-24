#!/usr/bin/env python3


def affichage_donnees(panier_action, prix_panier_actions):
    print()
    print("NOM ACTION - PRIX - TAUX - BENEFICE", end="\n\n")

    benefice_action = []
    i = 1
    for element in panier_action:
        benefice_action.append(element["benefice"])
        if i == len(panier_action):
            print(
                f'{element["nom"]} - {element["prix"]} - {element["taux"]} - {element["benefice"]}',
                end="\n\n",
            )
        else:
            print(
                f'{element["nom"]} - {element["prix"]} - {element["taux"]} - {element["benefice"]}'
            )

        i += 1
    print(f"Le prix total du panier d'actions est de {prix_panier_actions} euros.")
    print(
        f"Bénéfice attendu à 2 ans : {round(sum(benefice_action), 2)} euros", end="\n\n"
    )


def affichage_temps(debut, fin):
    temps_execution = round(fin - debut, 2)
    print(f"Programme exécuté en {temps_execution}s")


def affichage_erreurs(erreur_trouvees):
    if erreur_trouvees > 0:
        print(
            f"{erreur_trouvees} erreurs ont été trouvées dans le fichier de données.",
            end="\n\n",
        )
    else:
        return print()
