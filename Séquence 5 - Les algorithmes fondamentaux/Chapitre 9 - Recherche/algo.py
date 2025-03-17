import time
import
# compteur d'opération qui fait plus 1 à chaque opération élémentaire
# un générate liste qui génère une liste aléatoire, de nombre différents, dans l'ordre croissant
# fin : liste de T avec un n qui a évolué et en abcisse : N et en ordonnée : grand T

def generate_list(n):
    return 

def mesure_temps(fonction, tab, x):
    debut = time.perf_counter()
    fonction(tab, x) 
    fin = time.perf_counter()
    return fin - debut 

def recherche_sequentielle(tab:list, x) -> bool:
    for element in tab:
        if (element == x):
            print(f"{x} est dans la liste")
            return True
    print(f"{x} n'est pas dans la liste")
    return False

def recherche_dichotomique(tab:list, x:int) -> bool:
    gauche, droite = 0, len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2 # pas len car len est relatif au tableau entier
        if tab[milieu] == x: 
            print(f"{x} est dans la liste")
            return True
        elif tab[milieu] < x:
            gauche = milieu + 1  
        else:
            droite = milieu - 1 
    print(f"{x} n'est pas dans la liste")
    return False

x = 26
liste =  generate_list(10000000)
temps_seq = mesure_temps(recherche_sequentielle,liste, x)
temps_dicho = mesure_temps(recherche_dichotomique, liste, x)

print(f"Temps de recherche séquentielle: {temps_seq:.10f} secondes")
print(f"Temps de recherche dichotomique: {temps_dicho:.10f} secondes")

