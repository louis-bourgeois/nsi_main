def trouverExtremes(liste: list):
    maximum = 0
    minimum = 0
    for item in liste:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum
    return (minimum, maximum)


print(trouverExtremes([0, 1, 2, 4, 5, 6, 4, 7, 85, 4, 4, 4654, 111, 8]))


def remplacerParMoyenne(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    for i in range(len(liste)):
        if liste[i] <= moyenne:
            print(i)
            liste[i] = moyenne
    return moyenne, liste


print(remplacerParMoyenne([0, 1, 2, 4, 5, 6, 4, 7, 85, 4, 4, 4654, 111, 8]))
