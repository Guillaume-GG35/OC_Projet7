#!/usr/bin/env python3

import csv
import view
import constantes


def conversion_taux(texte_taux):
    return round(float(texte_taux[:-1]) / 100, 2)


def calcul_benefice(prix, taux):
    return round(prix * taux, 2)


fichier_data = view.choix_donnees()
chemin_fichier = constantes.chemin_fichier(fichier_data)

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
            if action["prix"] <= 0:
                erreur_trouvees += 1
                continue
        except ValueError:
            erreur_trouvees += 1
            continue

        action["taux"] = conversion_taux(ligne[2])
        action["benefice"] = calcul_benefice(action["prix"], action["taux"])
        liste_actions.append(action)

liste_actions_triee = sorted(liste_actions, key=lambda dict: dict["taux"], reverse=True)

panier_action = []
prix_panier_actions = 0
i = 0
while prix_panier_actions <= 500:
    if i == len(liste_actions_triee):
        break

    if prix_panier_actions + liste_actions_triee[i]["prix"] > 500:
        if (
            liste_actions_triee[j]["benefice"] < liste_actions_triee[i]["benefice"]
            and prix_panier_actions
            + liste_actions_triee[i]["prix"]
            - liste_actions_triee[j]["prix"]
            <= 500
        ):
            prix_panier_actions -= liste_actions_triee[j]["prix"]
            prix_panier_actions += liste_actions_triee[i]["prix"]
            panier_action.pop()
            panier_action.append(liste_actions_triee[i])
            j = i

    if prix_panier_actions + liste_actions_triee[i]["prix"] <= 500:
        prix_panier_actions += liste_actions_triee[i]["prix"]
        panier_action.append(liste_actions_triee[i])
        j = i
    i += 1


prix_panier_actions = round(prix_panier_actions, 2)

panier_action_trie = []
for element in liste_actions:
    if element in panier_action:
        panier_action_trie.append(element)

view.affichage_donnees(panier_action_trie, prix_panier_actions)
view.affichage_temps(DEBUT, constantes.fin())
view.affichage_erreurs(erreur_trouvees)
