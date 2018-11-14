from random import randrange
from math import ceil

argent = 1000
continuer = True

while continuer:
    print("Vous partez avec ", argent, "€ !")
    numero_choisi = input("Choisissez un numéro entre 0 et 49    ")

    try:
        numero_choisi = int(numero_choisi)
        assert (numero_choisi >= 0) and (numero_choisi < 50)
    except ValueError:
        print("Le Nombre doit être supérieur ou égal à 0 ou inférieur à 50!")
    numero_tire = randrange(50)

    mise = 0

    while (mise <= 0) or (mise > argent):

        if mise <= 0:
            print("Mise infèrieur ou égal à 0 !")

        mise = input("Quelle est votre mise ?     ")

    try:
        mise = int(mise)
        assert mise
    except AssertionError:
        print(" Il faut que ça soit un Nombre")

    print("Le Nombre Tiré est....... : Le ", numero_tire, "!")

    if numero_choisi == numero_tire:
        print("NUMERO GAGNANT ! Vous remportez 3 fois votre mise !")
        argent = argent + mise * 3
        print("Nouveau Solde: ", argent, "€")

    else:
        if numero_choisi % 2 == numero_tire % 2:
            mise = ceil(mise * 0.5)
            argent = argent + mise
            print(
                "Bonne Couleur, Vous ne eprdez que la moitié de votre mise ! \n Votre solde est maintenant à hauteur de: ",
                argent, "€")
        else:
            argent = argent - mise
            print("Perdu ! \n Votre solde est maintenant à hauteur de : ", argent, "€")

    if argent <= 0:
        print("Vous n'avez plus d'argent pour continuer ! Vous qujittez le Casino ")
        continuer = False

    carry = input("Vous voulez vous continuez ? O/N")

    if carry == "O":
        continuer = True
    elif carry == "N":
        continuer = False
