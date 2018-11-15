from random import randrange
from math import ceil

argent = 1000
continuer = True

while continuer == True:

    print("Vous partez avec ", argent, "€ !")
    numero_choisi= -1

    while (numero_choisi < 0) or (numero_choisi > 49):

        numero_choisi = input("Choisissez un numéro entre 0 et 49  :  ")

        try:
            numero_choisi = int(numero_choisi)
        except ValueError:
            print("Vuos n'avez pas saisi de nombre !")
            numero_choisi = -1
            continue
        if(numero_choisi > 49):
            print("Le  Numéro est superieur à 49 !")
            continue
        if(numero_choisi < 0):
            print("Le Numéro est Négatif")
            continue

    mise = 0

    while mise <= 0 or mise > argent:
        mise = int(input("Quelle est votre mise ?     "))

        if mise <= 0:
            print("Mise infèrieur ou égal à 0 !")
        try:
            mise = int(mise)
        except ValueError:
            print(" Vous n'avez pas saisi de nombre")
            mise = -1
            continue #Permet de repartir à la ligne du for ou while

        if mise <= 0:
            print("La mise doit être supérieur à 0")
        if mise > argent:
            print("Vous ne pouvez pas miser autant, votre solde est de: ",argent, "€")


    numero_tire = randrange(50)
    print("Le Nombre Tiré est....... : Le ", numero_tire, "!")

    if numero_choisi == numero_tire:
        print("NUMERO GAGNANT ! Vous remportez 3 fois votre mise soit :",mise*3,"€ !")
        argent = argent + mise * 3
        print("Nouveau Solde: ", argent, "€")

    elif numero_choisi % 2 == numero_tire % 2:
            mise = ceil(mise * 0.5)
            argent = argent + mise
            print(
                "Bonne Couleur, Vous remportez la moitié de la mise soit ",mise/2,"€ !\n Votre solde est maintenant à hauteur de: ",
                argent, "€")
    else:
        argent = argent - mise
        print("Perdu ! \nVotre solde est maintenant à hauteur de : ", argent, "€")

    if argent <= 0:
        print("Vous n'avez plus d'argent pour continuer ! Vous quittez le Casino.... ")
        continuer = False

    else:
        carry = input("Vous voulez vous continuez ? o/n")

        if carry == "O" or carry == "o":
            continuer = True
        elif carry == "N" or carry == "n":
            continuer = False
            print("Vous nous quittez avec: ", argent,"€")
