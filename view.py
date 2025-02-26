#!/usr/bin/env python3

import constantes


def choix_donnees():
    print()
    print("Liste des fichiers de données disponibles :")
    for fichier in constantes.FICHIERS:
        print(fichier)
    print()
    selection_utilisateur = input("Selectionner le jeu de données souhaité : ")
    while selection_utilisateur not in constantes.FICHIERS:
        print("Fichier introuvable : Merci de vérifier votre saisie !")
        selection_utilisateur = input("Selectionner le jeu de données souhaité : ")
    return selection_utilisateur


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
    temps_execution = fin - debut

    if temps_execution < 1:
        temps_execution = round(temps_execution, 5)
    else:
        temps_execution = round(temps_execution, 2)

    print(f"Programme exécuté en {temps_execution}s")


def affichage_erreurs(erreur_trouvees):
    if erreur_trouvees > 0:
        print(
            f"{erreur_trouvees} erreurs ont été trouvées dans le fichier de données.",
            end="\n\n",
        )
    else:
        return print()


def avertissement():
    print("ATTENTION : Le fichier sélectionné est volumineux.")
    print(
        "Le programme n'est pas prévu pour un jeu de données d'entrées aussi important."
    )
    choix_utilisateur = input("Continuer? (O/n) : ")
    while choix_utilisateur != "O" and choix_utilisateur != "n":
        print("Merci de taper 'O' pour Oui ou 'n' pour Non.")
        choix_utilisateur = input("Continuer? (O/n) : ")
    return choix_utilisateur
