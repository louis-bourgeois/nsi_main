# import random

# universe = (1, 2, 4, 5, 6)


# def lancers():
#     results = []
#     for i in range(100000):
#         results.append(random.choice(universe) + random.choice(universe))
#     count_iterations(results)


# def count_iterations(results:list):
#     iterations_of_sum = []
#     for result_possible in range(2, 13):
#         iterations_of_sum.append(results.count(result_possible))
#     for iteration, frequence in enumerate(iterations_of_sum, start=1):
#         freq_percentage = frequence/len(results)*100
#         stars = round(freq_percentage)
#         print(stars * "*")
#         # print(f"somme = {iteration}: {frequence} tirages, probabilité = {freq_percentage}%")


# lancers()

# Version biennn optimisé

import random
from collections import Counter

# Définition de l'univers
universe = (1, 2, 4, 5, 6)


def lancers():
    # Générer les résultats des 100 000 lancers
    results = [random.choice(universe) + random.choice(universe)
               for _ in range(100000)]

    # Compter les fréquences des sommes
    count_iterations(results)


def count_iterations(results):
    # Utilisation de Counter pour compter les occurrences de chaque somme
    counts = Counter(results)

    total = len(results)
    # Affichage des résultats sous forme de graphique à base d'étoiles
    # Toutes les sommes possibles (2 à 12)
    for result_possible in range(2, 13):
        frequence = counts.get(result_possible, 0)
        freq_percentage = frequence / total * 100
        stars = round(freq_percentage)
        print(stars * "*")


lancers()


## Double écran / Chauffage