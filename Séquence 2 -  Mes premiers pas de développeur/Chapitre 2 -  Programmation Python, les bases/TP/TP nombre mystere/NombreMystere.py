from random import randint


def jeu(intervalle, attempts_chosen):
    random_number = randint(intervalle[0], intervalle[1])
    finished = False
    attempts = 0

    while not finished and attempts < attempts_chosen:
        try:
            print(f"Il vous reste {10 - attempts}")
            user_entry = int(input("Entrer le nombre : "))

            attempts += 1

            if user_entry > random_number:
                print("Moins")
            elif user_entry < random_number:
                print("Plus")
            else:
                print(f"Vous avez trouvé le nombre mystère, c'était {
                      random_number} !")
                finished = True

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    if not finished:
        print(f"Vous avez épuisé vos tentatives. Le nombre mystère était {
              random_number}.")


def choisir_difficulte():
    print("Choisissez un niveau de difficulté :")
    print("1. Facile (1-10, 5 tentatives)")
    print("2. Moyen (1-50, 7 tentatives)")
    print("3. Difficile (1-100, 10 tentatives)")

    choix = input("Votre choix (1, 2 ou 3) : ")

    if choix == '1':
        return (1, 10), 5
    elif choix == '2':
        return (1, 50), 7
    elif choix == '3':
        return (1, 100), 10
    else:
        print("Choix invalide. Veuillez réessayer.")
        return choisir_difficulte()


def main():
    intervalle, attempts_chosen = choisir_difficulte()
    jeu(intervalle, attempts_chosen)


if __name__ == "__main__":
    main()
