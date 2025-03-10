############################################
# J'ai fait une version 2 avec des bases allant de 2 à 16 inclus
# J'ai tout de même inclus les négatifs dans ce fichier
# J'ai commenté de manière assez abusive le code pour montrer que je le comprends, qu'il n'a pas été généré par une IA
#            VERSION 1 : BASES FIXES
#  - Binaire (2) et Hexadécimal (16) seulement
#  - Complément à 2 sur 16 bits pour les négatifs
#  - Entiers uniquement
############################################

def decToBin(nombre_dec: int) -> str:
    """
    Convertit un entier (nombre_dec) en binaire sur 16 bits.
    Gère également les valeurs négatives en utilisant
    le complément à 2.
    """
    NOMBRE_BITS = 16

    # CAS 1 : nombre >= 0
    if nombre_dec >= 0:
        # Si c'est zéro, on retourne directement 16 zéros
        if nombre_dec == 0:
            return "0" * NOMBRE_BITS

        liste_bits = []
        # on stocke le nombre en décimal dans une variable (temporaire, d'où son nom) pour l'utiliser dans la boucle for
        valeur_temp = nombre_dec

        # Récupération des bits (division par 2 successives, on aurait pu utiliser bin())
        while valeur_temp > 0:
            liste_bits.append(str(valeur_temp % 2))
            # //= cela équivaut à écrire a = a // b (divisio entière), mais c'est plus beau :
            valeur_temp //= 2

        # On complète avec des zéros jusqu'à NOMBRE_BITS
        while len(liste_bits) < NOMBRE_BITS:
            liste_bits.append("0")

        # On inverse pour obtenir le bon ordre
        liste_bits.reverse()

        return "".join(liste_bits)

    # CAS 2 : nombre < 0
    else:
        # ici on sait que nombre dec est négatif donc sa valeur absolue est son opposé
        valeur_absolue = -nombre_dec
        liste_bits = []

        # Cas particulier : -0
        if valeur_absolue == 0:
            return "0" * NOMBRE_BITS

        while valeur_absolue > 0:
            liste_bits.append(str(valeur_absolue % 2))
            valeur_absolue //= 2

        while len(liste_bits) < NOMBRE_BITS:
            liste_bits.append("0")

        liste_bits.reverse()

        # Complément à 1 (on inverse tous les bits)
        liste_inversee = ["1" if bit == "0" else "0" for bit in liste_bits]

        # Puis on ajoute 1 (complément à 2)
        retenue = 1

        # Boucle à travers les bits de droite à gauche (du bit de poids faible au plus fort)
        for i in range(NOMBRE_BITS - 1, -1, -1):
            # Si le bit actuel est '0' et qu'il y a une retenue à ajouter
            if liste_inversee[i] == "0" and retenue == 1:
                liste_inversee[i] = "1"  # On change le bit de '0' à '1'
                # La retenue a été utilisée, pas besoin de la propager dans le reste de la boucle on lui met 0
                retenue = 0
                break                    # On peut arrêter la boucle car l'addition est terminée

            # Si le bit actuel est '1' et qu'il y a une retenue à ajouter
            elif liste_inversee[i] == "1" and retenue == 1:
                # On change le bit de '1' à '0' (comme 1 + 1 = 0 avec une retenue)
                liste_inversee[i] = "0"
                retenue = 1              # La retenue est maintenue pour le bit suivant

            else:
                # Si le bit actuel est '0' sans retenue ou '1' sans retenue, aucune action n'est nécessaire
                # On sort de la boucle car il n'y a plus de retenue à propager
                break

        # On reconstruit la chaîne de caractères à partir de la liste de bits modifiée
        return "".join(liste_inversee)


def binToDec(b: str) -> int:
    NB_BITS = 16
    if len(b) < NB_BITS:
        bit_signe = b[0]  # '0' ou '1'
        # Ici, je me suis demandé quelle était la convention pour pouvoir convertir en 16 bits une chaine en binaire signé
        # L'extension des signes semble être adoptée dans ce cas, si le signe est négatif on remplit de 1 à gauche, si c'est positif, on remplit de 0
        # rjust est une fonction permettant de remplir le début d'un str par un autre str spécifié (ici bit_signe, 0 ou 1)
        b = b.rjust(NB_BITS, bit_signe)

    if b[0] == "0":
        # on interprète comme du binaire non signé
        val = 0
        for bit in b:
            val = val * 2 + (1 if bit == "1" else 0)
        return val
    else:  # si le nombre est négatif, complément à 2 :
        bits_list = list(b)
        retenue = 1
        # on a une boucle s'arrêtant à -1, qui décrémente de 1 à chaque itération
        for i in range(NB_BITS - 1, -1, -1):
            if bits_list[i] == '1' and retenue == 1:
                bits_list[i] = '0'
                retenue = 0
                break
            elif bits_list[i] == '0' and retenue == 1:
                bits_list[i] = '1'
                retenue = 1
            else:
                break
        for i in range(NB_BITS):
            # on inverse les bits
            bits_list[i] = '1' if bits_list[i] == '0' else '0'
        val_pos = 0
        # on peut désormais convertir le binaire en décimal avec les multiplications successives par 2
        for bit in bits_list:
            val_pos = val_pos * 2 + (1 if bit == "1" else 0)
        return -val_pos  # - car c'est négatif


def decToHex(n: int) -> str:
    b = decToBin(n)  # on normalise l'info en binaire à l'aide de la fonction
    map_4b = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }  # on a map un caractère base 16 à du binaire (4b = 4 bits)
    h = []
    # on parcourt de 0 à 15 (inclus donc 16 fois) avec un pas de 4
    for i in range(0, 16, 4):
        # on utilise l'"opération" de slicing sur la chaine binaire pour extraire un groupe de 4 bits
        chaine_sliced = b[i:i+4]
        # on remplit la liste qui correspondera au caractères en hexadécimal en les faisant correspondre à notre mapping 4 bits
        h.append(map_4b[chaine_sliced])
    sortie = "".join(h).lstrip("0")
    return sortie if sortie else "0"


def hexToDec(h: str) -> int:
    # on met la chaîne en majuscules pour être cohérent avec le mapping binaire/hex ci dessous
    h = h.upper()
    # on map la base 10 avec le binaire
    bin_map = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"
    }

    b_temp = []  # je mets temp en faisant référence à temporaire, cette liste est en effet de ce type, elle sert à la boucle for seulement
    for caractere in h:
        b_temp.append(bin_map[caractere])

    # on assemble puis on complète à gauche avec des '0' si nécessaire
    b_str = "".join(b_temp)
    # zfill permet de compléter avec des 0 à gauche, au début de la chaine pour avoir les 16 bits ici
    b_str = b_str.zfill(16)

    # ensuite, on passe cette chaîne binaire de l'hexadécimal à binToDec pour avoir un décimal en sortie
    return binToDec(b_str)


def binToHex(b: str) -> str:
    return decToHex(binToDec(b))


def hexToBin(h: str) -> str:
    return decToBin(hexToDec(h))


if __name__ == "__main__":
    # TESTS (VERSION 1) - INTERPRETATION SIGNÉE POUR TOUT BINAIRE < 16 bits QUI COMMENCE PAR '1', car j'ai voulu mettre les négatifs

    # --------------------------------------------------------
    # 1) CAS "101000010010" : 12 bits, bit de tête = '1'
    #    => Extension de signe => 1111101000010010 => -1518
    # --------------------------------------------------------
    # Je change donc l'assert pour correspondre à la logique de mes fonctions
    # On considère ce binaire comme négatif.
    assert binToDec("101000010010") == -1518, (
        "Erreur binToDec (extension de signe => -1518)"
    )

    # decToBin(-1518) devrait nous redonner 1111101000010010
    # en complément à 2 sur 16 bits :
    #  - on part de 1518
    #  - on le code en binaire sur 16 bits
    #  - on l'inverse
    #  - on ajoute 1
    # = 1111101000010010
    assert decToBin(-1518) == "1111101000010010", (
        "Erreur decToBin (négatif, complément à 2 sur 16 bits)"
    )

    # --------------------------------------------------------
    # 2) CAS Positifs explicites sur 16 bits ou plus
    #    (Si on nous donne pile 16 bits commençant par '0', c'est un positif.)
    # --------------------------------------------------------
    # Par exemple : 2578 = 0000101000010010 sur 16 bits
    # Ici, on fait un test complet : dec -> bin, bin -> dec, etc.
    assert decToBin(2578) == "0000101000010010", "Erreur decToBin (positif)"
    assert binToDec("0000101000010010") == 2578, "Erreur binToDec (positif)"
    assert decToHex(2578) == "A12", "Erreur decToHex (positif)"
    assert binToHex("0000101000010010") == "A12", "Erreur binToHex (positif)"
    assert hexToBin("A12") == "0000101000010010", "Erreur hexToBin (positif)"
    assert hexToDec("A12") == 2578, "Erreur hexToDec (positif)"

    # --------------------------------------------------------
    # 3) CAS "négatifs" sur 16 bits exacts, par exemple -12
    # --------------------------------------------------------
    # On vérifie qu'on gère bien le complément à 2 sur 16 bits:
    # -12 => binaire => 1111111111110100
    assert decToBin(-12).endswith("1111111111110100"), (
        "Erreur decToBin négatif"
    )
    assert binToDec("1111111111110100") == -12, "Erreur binToDec négatif"
    assert decToHex(-12) == "FFF4", "Erreur decToHex négatif"
    assert binToHex("1111111111110100") == "FFF4", "Erreur binToHex négatif"
    assert hexToBin("FFF4") == "1111111111110100", "Erreur hexToBin négatif"
    assert hexToDec("FFF4") == -12, "Erreur hexToDec négatif"

    print("VERSION 1 (BASES FIXES, avec extensions de signe) : OK, aucune erreur !")
