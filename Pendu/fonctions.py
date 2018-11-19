import os
import pickle
from random import choice
from Pendu.donnees import *

#Gestion Score

def recup_scores():

        if os.path.exists(nom_fichier_score):
            fichier_scores = open(nom_fichier_score,"rb")
            mon_depickler = pickle.Unpickler(fichier_scores)
            scores = mon_depickler.load()
            fichier_scores.close()

        else:
            scores = {}

        return scores

def enregristrer_score(scores):
    fichier_score = open(nom_fichier_score,"wb")
    mon_pickler = pickle.Pickler(fichier_score)
    mon_pickler.dump(scores)
    fichier_score.close()


def recup_utilisateur():
    """
    Va servir a retourner le nom de l'utilisateur
    :return: nom de l'utilisateur
    """



def bonne_lettre(mot,lettre):
    if lettre in mot:
        return True
    else:
        return False

def nb_mot(mot): # nombre de lettres
    nb = 0
    for lettre in mot:
        nb += 1

    return nb


def mot_fini(mot, decouvert):               #decouvert= nb de lettre decouvert
    if nb_mot(mot) == decouvert:
        return True
    else:
        return False
