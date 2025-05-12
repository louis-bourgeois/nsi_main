objets_en_cale = [
    {"nom" : "malle d'or", "poids" : 150, "valeur" : 1500},
    {"nom" : "malle de perles", "poids" : 100, "valeur" : 800},
    {"nom" : "tonneau de rhum", "poids" : 40, "valeur" : 600},
    {"nom" : "malle de rubis", "poids" : 120, "valeur" : 2000},
    {"nom" : "malle de diamants", "poids" : 100, "valeur" : 25000},
    {"nom" : "malle d'épices", "poids" : 25, "valeur" : 3500},
    {"nom" : "coffre d'armes", "poids" : 120, "valeur" : 850},
    {"nom" : "tonneau de viandes séchées", "poids" : 10, "valeur" : 200},
    {"nom" : "sac de sels", "poids" : 10, "valeur" : 20}
]


assert objets_en_cale[0]["nom"] == "malle d'or"
assert objets_en_cale[1]["poids"] == 100
assert objets_en_cale[3]["valeur"] == 2000

def naif(objets:list, min_weight:int=10, max_value:int=99999999999999):
    n = len(objets)
    combinaisons = []
    # Préparation des données
    for i in range(2**n):
        combinaisons.append(bin(i)[2:])
    for i in range(2**n):
        nb_bits_combinaison = len(combinaisons[i])
        
    
    print(combinaisons)

def glouton(objets:list, min_weight:int=10, max_value:int=99999999999999):
    pass


naif(objets_en_cale)
glouton(objets_en_cale)
