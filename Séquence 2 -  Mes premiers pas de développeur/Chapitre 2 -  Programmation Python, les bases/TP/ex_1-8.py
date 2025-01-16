# Exercice 1
A = 5
B = 3
C = A + B
A = 2
C = B - A
print("Exercice 1:")
print("a=", A, "b=", B, "c=", C, end=" yes sir \n", sep=" | ")
# end = qu'est-ce qu'il y aura à la fin de la ligne, par défaut, c'est \n
# sep = change le séparateur entre les values : par défaut c'est un espace
# \n = retour à la ligne dans une string
# Exercice 2
A = 2
B = 1
C = 6
B = A
C = B
A = C
print("Exercice 2:")
print(A, B, C)
print("\n")

# Exercice 3
val = 6
leDouble = val * 2
print("Exercice 3:")
print("le double de", val, "vaut", leDouble)
print("\n")

# Exercice 4
print("Exercice 4:")
try:
    nombre = float(input("Entrez un nombre : "))
    carre = nombre ** 2
    print("Le carré de", nombre, "est", carre)
except ValueError:
    print("Erreur : la valeur saisie n'est pas un nombre valide.")
print("\n")

# Exercice 5
try:
    prenom = input("Exercice 5 - Quel est votre prénom ? ")
    print("Bonjour,", prenom + " !")
except Exception as e:
    print(f"Erreur inattendue : {e}")
print("\n")

# Exercice 6
try:
    prix_ht_str = input("Exercice 6 - Entrez le prix HT de l'article : ")

    # Remplacer les virgules par des points
    has_multiple_commas = prix_ht_str.count(",") > 1
    prix_ht_str = prix_ht_str.replace(",", ".")

    if has_multiple_commas:
        print("Erreur : plusieurs virgules trouvées.")
    else:
        prix_ht = float(prix_ht_str)

    quantite = int(input("Entrez le nombre d'articles : "))
    taux_tva = float(input("Entrez le taux de TVA (en %) : "))

    prix_total_ht = prix_ht * quantite
    if taux_tva > 20:
        print("Erreur : le taux de TVA ne peut pas dépasser 20%.")
    else:
        montant_tva = prix_total_ht * (taux_tva / 100)
        prix_total_ttc = prix_total_ht + montant_tva
        print("\n--- Facture ---",)
        print("Prix total HT :", prix_total_ht, "€")
        print("Montant de la TVA :", montant_tva, "€")
        print("Prix total TTC :", prix_total_ttc, "€")
except ValueError as ve:
    print("Erreur de saisie numérique : ", ve)
except Exception as e:
    print(f"Erreur inattendue : {e}")
print("\n")

# Exercice 7
try:
    nombre = float(input("Exercice 7 - Entrez un nombre : "))

    if nombre > 0:
        print("Le nombre est positif.")
    elif nombre < 0:
        print("Le nombre est négatif.")
    else:
        print("Le nombre est zéro.")
except ValueError:
    print("Erreur : la valeur saisie n'est pas un nombre valide.")
print("\n")

# Exercice 8
try:
    age = int(input("Exercice 8 - Entrez l'âge de l'enfant : "))

    if 6 <= age <= 7:
        categorie = "Poussin"
    elif 8 <= age <= 9:
        categorie = "Pupille"
    elif 10 <= age <= 11:
        categorie = "Minime"
    elif age >= 12:
        categorie = "Cadet"
    else:
        categorie = "Aucune catégorie"

    print("Catégorie :", categorie)
except ValueError:
    print("Erreur : l'âge doit être un nombre entier.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
