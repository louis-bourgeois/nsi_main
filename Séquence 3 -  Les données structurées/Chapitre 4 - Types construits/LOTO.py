import random

import matplotlib.pyplot as plt

# Draw = un tirage en anglais

def init_loto():
    """On initialise les résultats possibles, en demandant à l'user et en vérifiant """
    while True:
        try:
            total_numbers = int(
                input("Entrez le nombre total de numéros du loto (ex : 50) : "))
            if total_numbers <= 0:
                raise ValueError(
                    "Le nombre total de numéros doit être supérieur à 0.")
            numbers = list(range(1, total_numbers + 1))
            return numbers
        except ValueError as e:
            print(f"Erreur : {e} Veuillez entrer un nombre entier positif.")


def get_number_of_draws():
    """Ici on demande le nombre de tirages que le script va simuler, et on vérifie avec une ValueError"""
    while True:
        try:
            nb_draws = int(
                input("Entrez le nombre de tirages à simuler (ex : 10000) : "))
            if nb_draws <= 0:
                raise ValueError(
                    "Le nombre de tirages doit être supérieur à 0.")
            return nb_draws
        except ValueError as e:
            print(f"Erreur : {e} Veuillez entrer un nombre entier positif.")


def get_draw_size(total_numbers: int):
    """Ici, on demande le nombre de numéros par tirages et on vérifie"""
    while True:
        try:
            n = int(
                input(f"Entrez le nombre de numéros à tirer par tirage (ex : 5) : "))
            if n <= 0 or n > total_numbers:
                raise ValueError(f"Le nombre de numéros doit être entre 1 et {total_numbers}.")
            return n
        except ValueError as e:
            print(f"Erreur : {e} Veuillez entrer un nombre valide.")


def simulate_draws(numbers: list, n: int, nb_draws: int):
    """Là on simle un nombre donné de tirages et calcule les fréquences des numéros."""
    stats = [[number, 0] for number in numbers]
    for _ in range(nb_draws):
        result = random.sample(numbers, n)
        for num in result:
            stats[num - 1][1] += 1
    return stats


def plot_stats(stats: list):
    """On qffiche les statistiques de fréquence avec un histogramme."""
    numbers = [item[0] for item in stats]
    frequencies = [item[1] for item in stats]
    plt.bar(numbers, frequencies)
    plt.xlabel('Numéros du Loto')
    plt.ylabel('Fréquence')
    plt.title('Fréquence des Numéros du Loto après simulations')
    plt.show()


def main():
    print("Bienvenue dans le simulateur de tirage du loto.")

    numbers = init_loto()
    total_numbers = len(numbers)
    n = get_draw_size(total_numbers)
    nb_draws = get_number_of_draws()

    stats = simulate_draws(numbers, n, nb_draws)
    plot_stats(stats)


if __name__ == "__main__":
    main()
