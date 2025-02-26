#!/usr/bin/env python3

import os
import time

DOSSIER_DATA = os.path.join("data")
FICHIERS = os.listdir(DOSSIER_DATA)


def chemin_fichier(fichier):
    CHEMIN_FICHIER = os.path.join("data", fichier)
    return CHEMIN_FICHIER


def debut():
    DEBUT = time.time()
    return DEBUT


def fin():
    FIN = time.time()
    return FIN
