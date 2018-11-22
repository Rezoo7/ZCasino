from Pendu.fonctions import *
from Pendu.donnees import *


print( "Bienvenu sur le jeu du Pendu !")
print("\n\n Je choisis un mot au hasard....")


mot_choisi = choisir_mot()

utilisateur = recup_utilisateur()
scores = recup_scores()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0


continuer_partie = 'o'

while continuer_partie == 'o':

    print("Sccore du joueur : {0} => {1} ".format(utilisateur,scores[utilisateur]))

    mot_a_trouver = choisir_mot()
    lettres_trouve = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouve)
    nb_chances = nombre_coups

    verif = True

    while mot_a_trouver != mot_trouve and nb_chances>0:

        print("Mot à trouver : {0} , Il reste {1} chance(s) ".format(mot_trouve, nb_chances))
        lettre = recup_lettre()

        if lettre in lettres_trouve:
            print("Vous avez déja trouvé cette lettre ! ")
        elif lettre in mot_a_trouver:
            print("Bravo! La lettre est présente dans le mot")
            lettres_trouve.append(lettre)
        else:
            nb_chances -=1
            print("La lettre n'est pas présent dans le mot dommage !")
            mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouve)





    if mot_a_trouver == mot_trouve:
        print("Félicitations vous avez trouver le mot -> {0}!".format(mot_a_trouver))
    else:
        print ("PENDU !! Vous avez perdu !")


    scores[utilisateur] += nb_chances


    continuer_partie = input("Voulez vous continuer la partie ? (o/n")
    continuer_partie = continuer_partie.lower()

#la partie est finie on enregistre les scores

enregristrer_score(scores)

print("Vous finissez la partie avec {0} points".format(scores[utilisateur]))



