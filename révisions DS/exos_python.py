liste = []
for i in range(1,11):
    liste.append(i)

liste_2 = [i for i in range(1, 11)]
print(liste, liste_2)
liste.append(11)
liste.insert(0, 0) # attention j'avais oublié insert

liste.pop(-1) # pas obligé de mettre -1 

nombre2 = [i for i in range(1, 11, 3)]

# 2

# def exercice2():
#     liste = [12, 5, 8, 20, 33, 10, 3, 7]
    
#     resultat = []
#     for i in liste:
#         if i % 2 == 0:
#             resultat.append(i)
#     final_result = []
#     for i in resultat:
#         final_result.append(i**2) 
#     print(resultat)   
#     print(final_result)
#     maximum = final_result[0]
#     minimum = final_result[0]
#     for i in final_result:
#         if maximum <= i:
#             maximum = i
#         elif minimum >= i:
#             minimum = i
#     print(maximum, minimum)        

# correction 
def exercice2():
    # 1. Créer une liste de nombres
    nombres = [12, 5, 8, 20, 33, 10, 3, 7]
    
    # 2. Filtrer et afficher les nombres pairs
    pairs = [n for n in nombres if n % 2 == 0] # le if après pour avoir des conditions
    print("Nombres pairs:", pairs)
    
    # 3. Créer une nouvelle liste avec le carré de chaque élément pair
    carres = [n ** 2 for n in pairs]
    print("Carrés des nombres pairs:", carres)
    
    # 4. Calculer le maximum et le minimum sans utiliser min() et max()
    maximum = carres[0]
    minimum = carres[0]
    for n in carres[1:]: # je commence à partir du premier index : plus optimisé
        if n > maximum: # strictement
            maximum = n
        if n < minimum:
            minimum = n
    print("Maximum:", maximum, "| Minimum:", minimum)

exercice2()


# exercice 3

def exercice3():
    tuple_ = (45.75, 4.83)
    try:
        tuple_[0] = 45.00
    except TypeError as e:
        print("Erreur lors de la modification du tuple:", e)

    lat, long = tuple_[0], tuple_[1] # c'est faux
    # correction : 
    lat, long = tuple_


# On ne peut pas modifer la valeur d'un tuple
# exercice 4
def exercice4(): 
    etudiant = {
        "Nom" : "Ali", 
        "Age": 21,
        "Matière préférée" : "Mathématiques"
    }
    etudiant["Moyenne"] = 15.8
    etudiant["Age"] = 22
    for (key, value) in etudiant.items(): # oublie
        print(f"{key} : {value}")

# Exercice 5
def exercice5():
    classe = {
    "Ahmed": [15, 17, 14, 12],

    "Leila": [18, 16, 19, 14],

    "Yassine": [10, 12, 9, 11]
    }
    notes_leila = classe["Leila"]
    print(notes_leila)

    classe["Ahmed"].append(20)

    moyennes = []
    for name, grades in classe.items():
        somme = 0
        for grade in grades:
            somme += grade
        moyennes.append((name, (somme/len(grades)))) 
    print(moyennes)

exercice5()

# Exercice 6

# def exercice6(): 
#     noms = ["Ali", "Sami", "Leila"]
#     notes = [15, 18, 12]
#     dico = {}
#     i = 0
#     for name in noms :
#         dico[name] = notes[i]
#         i+=1

#     print(dico)

# Correction :
def exercice6():
    # 1. Créer deux listes et les fusionner en un dictionnaire
    noms = ["Ali", "Sami", "Leila"]
    notes = [15, 18, 12]
    
    # Utilisation de zip pour associer chaque nom à sa note
    resultats = {nom: note for nom, note in zip(noms, notes)}
    print("Résultats:", resultats)


exercice6()