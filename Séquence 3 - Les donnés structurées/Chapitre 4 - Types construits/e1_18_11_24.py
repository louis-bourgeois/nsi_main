liste = [8, 3, 6, 9, 1, 4, 17, 0, 11]


def aff_tab_1(tab: list):
    i = 0
    while i < len(tab):
        print(tab[i])
        i += 1


def aff_tab_2(tab: list):
    for i in range(len(tab)):
        print(i)


def aff_tab_3(tab: list):
    for i in tab:
        print(i)


def moyenne(notes: list):
    somme = 0
    for note in notes:
        somme += note
    return somme/len(notes)


def somme_pairs(nombres: list):
    somme = 0
    for nb in nombres:
        if nb % 2 == 0:
            somme += nb
    return somme


def min(nombres: list):
    x = nombres[0]
    for nb in nombres:
        if nb < x:
            x = nb
    return x


def max(nombres: list):
    x = nombres[0]
    for nb in nombres:
        if nb > x:
            x = nb
    return x




