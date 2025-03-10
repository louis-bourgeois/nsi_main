pokemons = {
    "Bulbizarre": {
        "id": 1,
        "types": ["plante", "poison"],
        "taille": 0.7,
        "poids": 6.9,
        "categorie": "graine",
        "faiblesses": {"feu": 1, "glace": 1, "vol": 0.5, "psy": 1},
        "talent": "engrais",
        "sexe": "both",
        "description": "Au début de sa vie, il se nourrit des nutriments accumulés dans la graine sur son dos. Cela lui permet de grandir.",
        "stats": {
            "pv": 3,
            "attaque": 3,
            "defense": 3,
            "att_spe": 4,
            "def_spe": 4,
            "vitesse": 3
        }
    },
    "Pikachu": {
        "id": 25,
        "types": ["electrik"],
        "taille": 0.4,
        "poids": 6.0,
        "categorie": "Souris",
        "faiblesses": {"sol": 1},
        "talent": "Statik",
        "sexe": "both",
        "description": "Quand il s’énerve, il libère instantanément l’énergie emmagasinée dans les poches de ses joues.",
        "stats": {
            "pv": 3,
            "attaque": 4,
            "defense": 3,
            "att_spe": 3,
            "def_spe": 3,
            "vitesse": 6
        }
    },
}


def ajouter_pokemon(nom, numero, types, taille, poids, categorie, faiblesses, talent, sexe, description, stats):
    for nom_existants in pokemons:
        if nom_existants == nom:
            print(
                "Oops, ce Pokémon existe déjà et ce pokédex n'est pas fait pour ça ! Annulation.......")
            return False
    pokemons[nom] = {
        "id": numero,
        "types": types,
        "taille": taille,
        "poids": poids,
        "categorie": categorie,
        "faiblesses": faiblesses,
        "talent": talent,
        "sexe": sexe,
        "description": description,
        "stats": stats
    }
    return True


def afficher_tous(pokemons):
    if len(pokemons) == 0:
        print("Aucun Pokémon dans le Pokédex.")
        return
    for nom_pokemon, infos_pokemon in pokemons.items():
        print("\n****", nom_pokemon, "****")
        for cle, valeur in infos_pokemon.items():
            print("    -", cle, "->", valeur)


def rechercher_par_nom(pokemons, nom):
    for cle, valeur in pokemons.items():
        if cle == nom:
            return valeur  # Je ne retourne pas le nom avec la cle, on le connait déjà
    return None


def rechercher_par_id(pokemons, numero):
    for cle, valeur in pokemons.items():
        if valeur["id"] == numero:
            return (cle, valeur)
    return None


def demander_entier(message):
    while True:
        reponse = input(message)
        try:
            return int(reponse)
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier")


def demander_flottant(message):
    while True:
        reponse = input(message)
        try:
            return float(reponse)
        except ValueError:
            print("Erreur : veuillez entrer un nombre réel")


def menu_principal():
    en_cours = True
    while en_cours:
        print("\n********************")
        print("Bienvenue dans votre Pokedex")
        print("Options:")
        print("1. Créer un Pokémon")
        print("2. Rechercher un Pokémon par numéro")
        print("3. Rechercher un Pokémon par nom")
        print("4. Afficher tous les Pokémons")
        print("5. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            nom = input("Nom : ")
            numero = demander_entier("Numéro : ")
            types_texte = input(
                "Entrez les types (séparés par des virgules) : ")
            types_liste = types_texte.split(",")
            taille = demander_flottant("Taille (en m) : ")
            poids = demander_flottant("Poids (en kg) : ")
            categorie = input("Catégorie : ")
            faiblesse_dico = {}
            nb_faib = demander_entier("Combien de faiblesses a ce pokemon ? ")
            for i in range(nb_faib):
                type_faiblesse = input("Type de la faiblesse : ")
                coef_faiblesse = input(
                    "Coefficient de la faiblesse (défaut=1) : ")
                try:
                    coef_numerique = float(coef_faiblesse)
                except ValueError:
                    coef_numerique = 1
                faiblesse_dico[type_faiblesse] = coef_numerique
            talent = input("Talent : ")
            sexe = input("Sexe : ")
            description = input("Description du Pokémon : ")

            pv = demander_entier("Points de vie (pv) : ")
            attaque = demander_entier("Attaque : ")
            defense = demander_entier("Défense : ")
            att_spe = demander_entier("Attaque spéciale : ")
            def_spe = demander_entier("Défense spéciale : ")
            vitesse = demander_entier("Vitesse : ")

            stats_pokemon = {
                "pv": pv,
                "attaque": attaque,
                "defense": defense,
                "att_spe": att_spe,
                "def_spe": def_spe,
                "vitesse": vitesse
            }

            succes = ajouter_pokemon(
                nom,
                numero,
                types_liste,
                taille,
                poids,
                categorie,
                faiblesse_dico,
                talent,
                sexe,
                description,
                stats_pokemon
            )
            if succes:
                print(nom, "ajouté avec succès !")
        elif choix == "2":
            numero = demander_entier("Numéro (id) du Pokémon : ")
            trouve = rechercher_par_id(pokemons, numero)
            if trouve:
                nom_pokemon, info = trouve
                print("\nInfos pour", nom_pokemon,
                      "(id=" + str(numero) + ") :")
                for cle, val in info.items():
                    print("-", cle, ":", val)
            else:
                print("Aucun Pokémon avec ce numéro")
        elif choix == "3":
            # j'applique quelques fonctions permettant de clean l'entrée et de plus efficacement géré des fautes de majuscules ou d'espace
            nom_poke = input("Nom du Pokémon : ").strip().capitalize()
            data = rechercher_par_nom(pokemons, nom_poke)
            if data:
                print("\nInfos pour", nom_poke, ":")
                for cle, val in data.items():
                    print("-", cle, ":", val)
            else:
                print(
                    "Aucun Pokémon ne correspond à ce nom, deviens meilleur et tu l'obtiendras peut-être...")
        elif choix == "4":
            afficher_tous(pokemons)
        elif choix == "5":
            print("Fermeture du Pokedex..... A la revoyure !")
            en_cours = False
        else:
            print("Mmmmmmh, choix invalide, réessaye.")


if __name__ == "__main__":
    menu_principal()


# Je me suis permis d'ajouter une gestion d'erreurs robuste et d'ajouter des fonctions permettant d'éviter la redondance pour les inputs du menu
