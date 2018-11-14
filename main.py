from random import *


argent = 1000
continuer = True

while continuer:
    print("Vous partez avec ",argent,"€ !")
    numero_choisi = input("Choisissez un numéro entre 0 et 49    ")

    try:
        numero_choisi = int(numero_choisi)
        assert (numero_choisi >= 0) and (numero_choisi< 50)
    except ValueError:
        print("Le Nombre doit être supérieur ou égal à 0 ou inférieur à 50!")
    numero_tire = randrange(50)

    mise = input("Quelle est votre mise ?     ")

    try:
        mise = int(mise)
        assert mise
    except AssertionError:
        print(" Il faut que ça soit un Nombre")

    print("Le Nombre Tiré est....... : Le ", numero_tire, "!")

    if numero_choisi == numero_tire:
        mise = mise * 3
    else:
        if (numero_choisi % 2 == 0) and (numero_tire % 2 == 0) or (numero_choisi % 2 != 0) and (numero_tire % 2 != 0):
            argent = argent - mise * 0.5
            print("Votre solde est maintenant à hauteur de: ", argent, "€")
        else:
            argent = argent - mise
            print("Votre solde est maintenant à hauteur de : ",argent, "€")

    carry = input("Vous voulez vous continuez ? O/N")

    if carry == "O":
        continuer = True
    elif carry == "N":
        continuer = False

