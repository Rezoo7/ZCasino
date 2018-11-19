def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu est un flottant !")

    print("Votre flottant de base: ", flottant)
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")

    print("Après transformation : ")
    return ",".join([partie_entiere, partie_flottante[:3]])


liste = [0, 1, 2, 3, 4, 5]
liste_c = [nb * nb * nb  for nb in liste if nb*nb*nb > 3  ]
#print(liste_c)

inventaire = [
  ("pommes", 22),
  ("melons", 4),
  ("poires", 18),
  ("fraises", 76),
  ("prunes", 51),
]

inventaire_inverse = [(nb,fruit) for fruit,nb in inventaire]
inventaire = [ (fruit,nb) for nb,fruit in sorted(inventaire_inverse,reverse = True )]
#print(inventaire)


dico = dict()
dico["pseudo"] = "rezoo"
dico["mdp"] = "****"
print(dico)

#del dico["mdp"]   # " " "
# dico.pop("mdp") #necessite de donner la clé pour supprimer
print("Supprimé: ", dico.pop("mdp")) #renvoie la valeur supprimée !

#print_bis = print #WHATTT on peut changer nom de la fonction !


