import random

import matplotlib.pyplot as plt


def init_loto():
    try:
        total_numbers = int(
            input("Entrez le nombre total de numéros du loto : "))
        numbers = list(range(1, total_numbers + 1))
    except ValueError:
        print("Erreur: rentrer un nombre, redémarrer le programme.")
        numbers = []
    return numbers


def simulate_tirage(numbers, n, num_draws):
    stats = [[number, 0] for number in numbers]
    for _ in range(num_draws):
        result = random.sample(numbers, n)
        for num in result:
            stats[num - 1][1] += 1
    return stats


def plot_stats(stats):
    numbers = [item[0] for item in stats]
    frequencies = [item[1] for item in stats]
    plt.bar(numbers, frequencies)
    plt.xlabel('Numéros du Loto')
    plt.ylabel('Fréquence')
    plt.title('Fréquence des Numéros du Loto après Simulations')
    plt.show()


def main():
    numbers = init_loto()
    if not numbers:
        return
    n = 5
    num_draws = 10000
    stats = simulate_tirage(numbers, n, num_draws)
    plot_stats(stats)


if __name__ == "__main__":
    main()
