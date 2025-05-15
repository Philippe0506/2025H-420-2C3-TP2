# utils.py

import csv
import json

def lire_csv(chemin):
    with open(chemin, "r", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier)

def sauvegarder_json(data, chemin):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(data, fichier)

def ecrire_texte(contenu, chemin):
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(contenu)
