# TP4 : Les chaînes de caractères

# Exercice 1
print("Exercice 1:")
chaine1 = "Le mot paix de par le monde"
longueur = len(chaine1)
print(f"Chaîne : \"{chaine1}\"")
print(f"Longueur de la chaîne : {longueur}")

print("Numéros Unicode des caractères :")
for index, caractere in enumerate(chaine1):
    print(f"Caractère '{caractere}' à la position {index} : {ord(caractere)}")
print("\n")

# Correction Ex 1, c'était bon aussi
for c in chaine1:
    print(c, "=>", ord(c))

# Exercice 2
print("Exercice 2:")
chaine2 = "Bonjour le monde"
caractere_recherche = 'e'
if caractere_recherche in chaine2:
    print(f"La chaîne \"{chaine2}\" contient le caractère '{
          caractere_recherche}'.")
else:
    print(f"La chaîne \"{chaine2}\" ne contient pas le caractère '{
          caractere_recherche}'.")
print("\n")

# Correction :


def exo2(chaine):
    for c in caractere_recherche:
        if c == "e":
            return "'e' est dans la chaine"
    return "'e' n'est pas dans la chaine"


# Exercice 3
print("Exercice 3:")
chaine3 = "L'été est une saison agréable."
compteur = chaine3.count('e')
print(f"Le caractère 'e' apparaît {
      compteur} fois dans la chaîne : \"{chaine3}\"")
print("\n")

# Exercice 4
# Correction


def exo4(chaine):
    resultat = ""
    for caractere in chaine:
        resultat += (f"{caractere}*")
    print(resultat[:-1])


exo4("EPID")

print("\n")
# Exercice 5
print("Exercice 5:")
chaine5 = "zorglub"
chaine_inverse = chaine5[::-1]
print(f"Chaîne originale : \"{chaine5}\"")
print(f"Chaîne inversée : \"{chaine_inverse}\"")
print("\n")

# Correction


def exo5(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    print(resultat)
