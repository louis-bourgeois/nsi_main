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

# Exercice 2
print("Exercice 2:")
chaine2 = "Bonjour le monde"
caractere_recherche = 'e'
if caractere_recherche in chaine2:
    print(f"La chaîne \"{chaine2}\" contient le caractère '{caractere_recherche}'.")
else:
    print(f"La chaîne \"{chaine2}\" ne contient pas le caractère '{caractere_recherche}'.")
print("\n")

# Exercice 3
print("Exercice 3:")
chaine3 = "L'été est une saison agréable."
compteur = chaine3.count('e')
print(f"Le caractère 'e' apparaît {compteur} fois dans la chaîne : \"{chaine3}\"")
print("\n")

# Exercice 4
print("Exercice 4:")
chaine4 = "EPID"
chaine_asterisques = "*".join(chaine4)
print(f"Chaîne originale : \"{chaine4}\"")
print(f"Chaîne avec astérisques : \"{chaine_asterisques}\"")
print("\n")

# Exercice 5
print("Exercice 5:")
chaine5 = "zorglub"
chaine_inverse = chaine5[::-1]
print(f"Chaîne originale : \"{chaine5}\"")
print(f"Chaîne inversée : \"{chaine_inverse}\"")
print("\n")

# Exercice 6 (BONUS)
print("Exercice 6 (BONUS):")
def est_palindrome(chaine):
    # Supprimer les espaces et les points, et convertir en minuscules
    chaine_nettoyee = ''.join(car for car in chaine if car.isalnum()).lower()
    return chaine_nettoyee == chaine_nettoyee[::-1]

chaine6 = "s.o.s"
if est_palindrome(chaine6):
    print(f"La chaîne \"{chaine6}\" est un palindrome.")
else:
    print(f"La chaîne \"{chaine6}\" n'est pas un palindrome.")

# Autres exemples de palindromes
exemples_palindromes = ["radar", "kayak", "été", "A man a plan a canal Panama"]
for exemple in exemples_palindromes:
    if est_palindrome(exemple):
        print(f"La chaîne \"{exemple}\" est un palindrome.")
    else:
        print(f"La chaîne \"{exemple}\" n'est pas un palindrome.")
