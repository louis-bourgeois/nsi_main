liste = []


characters = (
    "\n JEU DU PENDU \n",
    "    3",
    "________________",
    "|4 /           |5",
    "| /          6 O",
    "|         8 ___|____ 9",
    "|              | <======= 7",
    "| 2            |",
    "|             / \ ",
    "|          10/   \ 11",
    "|     1",
    "|_____________________",
    "\n"
)


def JOUER(lettre: str, mot: str):
    found = False
    for i in range(len(mot)):  # ou range(0,len(mot))
        if mot[i].lower() == lettre.lower():
            liste[i] = lettre
            found = True
    return found


def PENDU(mot: str, tentative: int = 10):
    for i in characters:
        print(i)
    for i in range(len(mot)):  # ou range(0, len(mot))
        liste.append("_")
    while tentative > 0 and "_" in liste:
        print(liste)
        print(f"Il te reste {tentative} tentatives \n")
        lettre = input("Essayez une lettre : ")
        if JOUER(lettre, mot) == False:
            tentative = tentative - 1
    if "_" in liste:
        print("\n GAME OVER ! \n")
        return False
    print("\n You've find the right word \n")
    return True


PENDU("Lapin")
play_again = True
while play_again:
    liste.clear()
    print("1 - Rejouer")
    print("2 - Quitter \n")
    response = input("Votre réponse : ")
    if response == "1":
        PENDU("Lapin")
    if response == "2":
        play_again = False
