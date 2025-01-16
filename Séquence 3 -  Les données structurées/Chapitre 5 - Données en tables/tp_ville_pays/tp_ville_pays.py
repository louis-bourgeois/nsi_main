# fonction importation d'un csv dans un dictionnaire de dictionnaires dont les clefs se situent dans la première ligne du CSV (les descripteurs)

# entrée le nom du fichier CSV

# sortie le dictionnaire de dictionnaires

def importation(fichier):

    file = open(fichier, "r", encoding="utf-8")

    table = {}
  
    descripteurs = file.readline()
    list_desc = descripteurs.rstrip().split(";")

    lignes = file.readlines()

    for ligne in lignes:
        ligne_dico = {}
        ligne = ligne.rstrip().split(";")
        for i in range(len(list_desc)):
            ligne_dico[list_desc[i]] = ligne[i]
        table[ligne[0]] = ligne_dico
    file.close()
    return table

countries = importation("countries.csv")


cities = importation("cities.csv")


# print(cities["FR-Dunkerque"]["Population"])

# print(countries["FR"]["Capital_Id"][3:])
# print(cities[countries["FR"]["Capital_Id"]["Name"]])

# print(cities["FR-Paris"]["Name"])

# 4.a et b 
def afficher(datas):
    print(datas)
    print(f"*** {datas["Name"]} ***")
    for key, value in datas.items():
        print(f"{key} : {value}")
    print("\n")


def afficherTout(datas):
    for val in datas.values():
        print(afficher(val))

def recherche(name, datas):
    for value in datas.values():
        if value["Name"].lower() == name.lower():
            return value

def nbPopulationFr():
    return countries["FR"]["Population"]   

def nbPopulation(pays_name):
    return countries[recherche(pays_name, countries)["ISO"]]["Population"]

def codesDollar():
    return [val["Currency_Code"] for val in countries.values() if val["Currency_Name"] == "Dollar"]

# def moyenneHabitantVille(cities, countries):
#     data = {}
#     for country in countries.values():
#         sum = 0
#         i = 0
#         for city in cities.values():
#             if city["Country_ISO"] == country["ISO"]:
#                 sum += int(country["Population"])
#                 i += 1
#         data[country["Name"]] = sum/i
#     return data

def moyenneHabitantVille():
    data = {}
    for iso, pays in countries.items():
        moyenne =  0
        i = 0
        for id_ville, ville in cities.items():
            moyenne+=ville["Population"]
            i += 1
        moyenne = moyenne / i


def top20paysPopulation(countries):
    liste_pays = []
    for pays in countries.values():
        liste_pays.append(pays["Population"])
    liste_pays.sort(reverse=True)      

    # Tri décroissant
    liste_pays.sort(key=lambda x: x[1], reverse=True)

    return liste_pays[:20]

def ajouterVille(cities, fichier, newCity):
    newRow = ""
    for info in newCity.values():
        newRow += f'{info};'
    newRow = newRow[:-1]+"\n"
    nomVille = newCity["Name"]
    cities[nomVille] = newCity

print(moyenneHabitantVille(cities, countries))

ajouterVille({"ID" : "AF-Wakanda",
              "Name" : "Wakanda",
              "Latitude": "0.0",
              "Longitude": "0.0",
              "Country_ISO" : "WA";
              "Population": "10000"
              })
# print(nbPopulationFr())
# afficher(recherche("France", countries))

