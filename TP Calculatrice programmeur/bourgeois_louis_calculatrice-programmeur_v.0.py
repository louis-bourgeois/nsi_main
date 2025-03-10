##########################################
# VERSION 0 : Minimal, sans négatifs
# Version de secours, pour m'assurer le 20 :)
##########################################

def binToDec(nb_bin: str) -> int:
    dec_value = 0
    for bit in nb_bin:
        dec_value = dec_value * 2 + int(bit)
    return dec_value


def decToBin(nb_dec: int) -> str:
    if nb_dec == 0:
        return "0"
    bits = []
    while nb_dec > 0:
        bits.append(str(nb_dec % 2))
        # //= revient à faire nb_dec = nb_dec // 2 (division entière)
        nb_dec //= 2
    bits.reverse()
    return  "".join(bits)


def binToHex(nb_bin: str) -> str:
    return decToHex(binToDec(nb_bin))


def hexToBin(nb_hex: str) -> str:
    return decToBin(hexToDec(nb_hex))


def decToHex(n: int) -> str:
    b = decToBin(n)  # je normalise en binaire
    # on s'assure que la longueur de b est multiple de 4
    #    (pour pouvoir la découper proprement en blocs de 4)
    padding = (4 - (len(b) % 4)) % 4

    b = b.zfill(len(b) + padding)

    # on crée un dictionnaire mappant 4 bits à un hexa
    map_4b = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }

    # on parcourt la chaîne binaire par groupes de 4
    h = []
    for i in range(0, len(b), 4):
        # on extrait les 4 bits de la chaine de décimal en à l'aide du slcing
        bloc4 = b[i:i+4]
        h.append(map_4b[bloc4])

    # on assemble la chaîne hexadécimale, puis on enlève d’éventuels '0' de tête
    sortie = "".join(h).lstrip("0")

    return sortie if sortie else "0"


def hexToDec(nb_hex: str) -> int:
    # on normalise en majuscules pour correspodre avec le mapping ci dessous
    nb_hex = nb_hex.upper()
    map_hex = "0123456789ABCDEF"
    dec_value = 0
    for char in nb_hex:
        dec_value = dec_value * 16 + map_hex.index(char)
    return dec_value


# ===== ZONE DE TESTS =====
if __name__ == "__main__":
    nb_bin_in = "101000010010"
    nb_dec_in = 2578
    nb_hex_in = "A12"

    assert binToDec(nb_bin_in) == 2578, "Erreur avec binToDec"
    assert decToBin(0) == "0", "Erreur avec decToBin"
    assert decToBin(nb_dec_in) == "101000010010", "Erreur avec decToBin"
    assert decToHex(nb_dec_in) == "A12", "Erreur avec decToHex"
    assert binToHex(nb_bin_in) == "A12", "Erreur avec binToHex"
    assert hexToBin(nb_hex_in) == "101000010010", "Erreur avec hexToBin"
    assert hexToDec(nb_hex_in) == 2578, "Erreur avec hexToDec"

    print("Version 0 : OK, aucune erreur !")
