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
    """
    :param scores:
    """

    fichier_score = open(nom_fichier_score,"wb")
    mon_pickler = pickle.Pickler(fichier_score)
    mon_pickler.dump(scores)
    fichier_score.close()


def recup_utilisateur():

    """
    Va servir a retourner le nom de l'utilisateur
    Si le nom n'est pas valide on appelle recursivement la methode
    :return: name , nom de l'utilisateur
    """

    nom = input("Saisissez votre pseudo : ")

    nom = nom.capitalize()
    if not nom.isalnum() or len(nom)<4:
        print("Pseudo Invalide ! Doit être sans espace (lettre et/ou Nombre) et superieur à 4 caractère")
        return recup_utilisateur()
    else:
        return nom


def recup_lettre():
    """Cette fonction récupère une lettre saisie par
        l'utilisateur. Si la chaîne récupérée n'est pas une lettre,
        on appelle récursivement la fonction jusqu'à obtenir une lettre"""

    lettre = input("Saisissez une lettre: ")
    lettre.lower()

    if not lettre.isalnum() or len(lettre) != 1:
        print("Ce n'est pas une lettre !")
        return recup_lettre()
    else:
        return lettre


def choisir_mot():
    """
    :return: le mot choisis dans la liste de mots
    """

    return choice(mots)


def recup_mot_masque(mot_complet, lettres_trouvees):

    """
    Cette fonction renvoie le mot masque en fonction de:
    :param mot_complet: le mot entier qui doit etre trouver
    :param lettres_trouvees: le lettres deja trouvees
    :return: mot_masque
    """
    mot_masque = ""

    for lettres in mot_complet:
        if lettres in lettres_trouvees:
            mot_masque += lettres
        else:
            mot_complet += "*"

    return mot_masque




