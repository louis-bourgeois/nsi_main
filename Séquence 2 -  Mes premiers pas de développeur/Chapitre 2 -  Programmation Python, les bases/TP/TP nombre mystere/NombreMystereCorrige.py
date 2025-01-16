from random import randint

nb_random = randint(1, 100)
nb_user = 0
nb_tentatives = 0

while nb_user != nb_random and nb_tentatives < 10:
    try:
        print(f"Il vous reste {10-nb_tentatives} tentatives")
        nb_user = int(input("Saisir un nombre 1 et 100 :"))
        if nb_user > nb_random:
            print("C'est -")
        else:
            print("C'est +")
    except ValueError:
        print("Mauvaise valeur")
        
if nb_user == nb_random:
    print("Vous avez gagné")
else:
    print(f"Vous avez perdu ! Le nombre mystère était : {nb_random}")
