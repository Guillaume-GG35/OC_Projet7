#!/usr/bin/env python3

import csv
import itertools
import view
import constantes


def conversion_taux(texte_taux):
    return round(float(texte_taux[:-1]) / 100, 2)


def calcul_benefice(prix, taux):
    return round(prix * taux, 2)


fichier_data = view.choix_donnees()
chemin_fichier = constantes.chemin_fichier(fichier_data)

with open(chemin_fichier, "r") as fichier:
    nombre_lignes = sum(1 for ligne in fichier)
    if nombre_lignes > 21:
        choix_utilisateur = view.avertissement()
        if choix_utilisateur == "n":
            exit()

DEBUT = constantes.debut()

with open(chemin_fichier, "r") as data_csv:
    lecteur = csv.reader(data_csv)

    liste_actions = []
    premiere_ligne = True
    erreur_trouvees = 0

    for ligne in lecteur:
        if premiere_ligne:
            premiere_ligne = False
            continue
        action = {}
        action["nom"] = ligne[0]

        try:
            action["prix"] = float(ligne[1])
            if action["prix"] < 0:
                erreur_trouvees += 1
                continue
        except ValueError:
            erreur_trouvees += 1
            continue

        action["taux"] = conversion_taux(ligne[2])
        action["benefice"] = calcul_benefice(action["prix"], action["taux"])
        liste_actions.append(action)

    liste_prix_actions = [element["prix"] for element in liste_actions]
    liste_benefice_actions = [element["benefice"] for element in liste_actions]

    tuple_prix_actions = tuple(liste_prix_actions)
    tuple_benefice_actions = tuple(liste_benefice_actions)

i = 1
liste_benefice_combinaison = []
meilleur_benefice = 0
while i <= len(liste_prix_actions):
    liste_combinaisons = itertools.combinations(liste_prix_actions, i)
    for combinaison in liste_combinaisons:
        if sum(combinaison) <= 500:
            benefice_action = []
            for prix in combinaison:
                index = tuple_prix_actions.index(prix)
                benefice_action.append(tuple_benefice_actions[index])

            if sum(benefice_action) > meilleur_benefice:
                meilleur_benefice = sum(benefice_action)
                liste_benefice_combinaison.append(benefice_action)
    i += 1

meilleure_combinaison = liste_benefice_combinaison[-1]
panier_action = []
for element in meilleure_combinaison:
    index = tuple_benefice_actions.index(element)
    panier_action.append(liste_actions[index])

prix_panier_actions = 0
for element in panier_action:
    prix_panier_actions += element["prix"]

prix_panier_actions = round(prix_panier_actions, 2)

view.affichage_donnees(panier_action, prix_panier_actions)
view.affichage_temps(DEBUT, constantes.fin())
view.affichage_erreurs(erreur_trouvees)
