# je n'ai pas partagé le code en fonction

import random

numbers = list(range(1000001))
random.shuffle(numbers)
# Méthode 1 (nul à chier) :

# result = []
# for i in range(5):
#     random.shuffle(numbers)
#     result.append(random.choice(numbers))
# print(result)

# Avec les fonctions :


def brassage(numbers):
    random.shuffle(numbers)
    return numbers


def tirage(numbers, n):
    print([random.choice(numbers) for _ in range(n)])


brassage(numbers)
tirage(numbers, 5)

# Méthode 2 (peut mieux faire) :

# result = [random.choice(numbers) for _ in range(5)]
# print(result)


# Méthode 3 : plus optimisée :

# result = random.sample(numbers, 5)
# print(result)
