import random

# # Définir l'univers des possibles
# universe = (1, 2, 4, 5, 6)

# # Fonction pour effectuer les lancers
# def lancers():
#     results = []
#     for _ in range(100000):
#         results.append(random.choice(universe) + random.choice(universe))
#     return results

# # Fonction pour compter les itérations et créer une matrice sans pandas
# def count_iterations_matrix(results):
#     result_range = range(2, 13)
#     total_results = len(results)

#     # Compter les fréquences
#     frequencies = {result: results.count(result) for result in result_range}

#     # Créer une matrice sous forme de liste
#     matrix = [["Somme", "Tirages", "Probabilité (%)"]]
#     for result, freq in frequencies.items():
#         probability = round((freq / total_results) * 100, 2)
#         matrix.append([result, freq, probability])

#     return matrix

# # Fonction pour afficher la matrice
# def display_matrix(matrix):
#     for row in matrix:
#         print("{:<10} {:<10} {:<10}".format(*row))

# # Effectuer les lancers et générer la matrice
# results = lancers()
# matrix = count_iterations_matrix(results)

# # Afficher la matrice
# display_matrix(matrix)

universe = (0, 1, 2, 4, 5, 6)


def lancer(nb_lancers=1000000000):
    results = []
    for i in range(2, 13):
        results.append([i, 0])
    print(results)
    for i in range(nb_lancers + 1):
        somme = random.choice(universe) + random.choice(universe)
        index = somme-2
        results[index][1] += 1
    print(results)


lancer()


# Version biennn optimisé

# import random
# from collections import Counter

# Définition de l'univers
# universe = (1, 2, 4, 5, 6)


# def lancers():
#     # Générer les résultats des 100 000 lancers
#     results = [random.choice(universe) + random.choice(universe)
#                for _ in range(100000)]

#     # Compter les fréquences des sommes
#     count_iterations(results)


# def count_iterations(results):
#     # Utilisation de Counter pour compter les occurrences de chaque somme
#     counts = Counter(results)

#     total = len(results)
#     # Affichage des résultats sous forme de graphique à base d'étoiles
#     # Toutes les sommes possibles (2 à 12)
#     for result_possible in range(2, 13):
#         frequence = counts.get(result_possible, 0)
#         freq_percentage = frequence / total * 100
#         stars = round(freq_percentage)
#         print(stars * "*")


# lancers()


# ## Double écran / Chauffage
