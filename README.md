# OC-Projet4 : Développez un programme logiciel en Python.

Ce programme permet d'analyser les différentes options d'achats d'actions afin de maximiser le profit réalisable.<br>
<br>
> [!NOTE]
> Testé sous Ubuntu 24.04 - Python 3.12.3

## Prérequis

Pour installer ce programme, vous aurez besoin d'une connexion internet. Le programme est ensuite exécuté en local et ne nécessite pas de connexion internet pour fonctionner.<br>
<br>
Python doit être installé sur votre ordinateur (version 3.12.3 ou supérieur).<br>
<br>

## Installation et exécution du programme

<details>
<summary>Etape 1 - Installer git</summary><br>

Pour télécharger ce programme, vérifiez que git est bien installé sur votre ordinateur.<br>
Vous pouvez l'installer en suivant les instructions fournies sur le site [git-scm.com](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

</details>

<details>
<summary>Etape 2 - Cloner le dépôt contenant le programme</summary><br>


Utilisez la commande suivante :

``git clone https://github.com/Guillaume-Gillon/OC_Projet7.git``

</details>

<details>
<summary>Etape 3 - Exécuter le programme</summary><br>

Pour exécuter le programme bruteforce, tapez la commande <br>
``python3 bruteforce.py``

Pour exécuter le programme optimisé, tapez la commande <br>
``python3 optimized.py``

</details>

## Fontionnement du programme

Le programme vous demande de choisir un set de données à analyser.
Les fichiers de données doivent être présents dans le répertoire **data**.

> [!NOTE]
> Les fichiers de données doivent impérativement être au format CSV.

Le programme bruteforce.py n'est pas prévu pour l'analyse d'une grande quantité de données.
Le programme optimized.py est moins précis mais accepte un volume de données plus important.
