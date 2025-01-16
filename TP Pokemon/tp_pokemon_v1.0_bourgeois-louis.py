pokemons = {
    "Bulbizarre": {
        "id": 1,
        "types": ["plante", "poison"],
        "taille": 0.7,
        "poids": 6.9,
        "categorie": "graine",
        "faiblesses": {"feu": 1, "glace": 1, "vol": 0.5, "psy": 1},
        "talent": "engrais",
        "sexe": "both"
    },
    "Pikachu": {
        "id": 25,
        "types": ["electrik"],
        "taille": 0.4,
        "poids": 6.0,
        "categorie": "Souris",
        "faiblesses": {"feu": 1, "glace": 1, "vol": 0.5, "psy": 1},
        "talent": "Statik",
        "sexe": "both"
    },
}


def add_pokemon(name: str, numero: int, types: list, taille: float, poids: float, categorie: str, faiblesses: dict, talent: str, sexe: str):
    pokemons[name] = {
        "id": numero,
        "type": types,
        "taille": taille,
        "poids": poids,
        "categorie": categorie,
        "faiblesses": faiblesses,
        "talent": talent,
        "sexe": sexe
    }


def display(pokemons: dict):
    for pokemon_name, pokemon_data in pokemons.items():
        print(f"**** {pokemon_name} ****")
        for key, value in pokemon_data.items():
            print(f"    - {key} -> {value}")


def search_by(pokemons, p_name_to_search, p_id=None, criteria="title"):
    for pokemon_name, pokemon_data in pokemons.items():
        if criteria == "title" and p_name_to_search != None:
            if pokemon_name == p_name_to_search:
                return pokemon_data
        else if criteria == "numero" and p_id != None:
            if pokemon_data["id"] == p_id
    print("Le pokémon ne figure pas dans la base de données.")


add_pokemon("bafeé", 20, ["plante"], 0.9, 0.5, "dzedz",
            {"dzdzd": 1}, "eddzd", "male")
search_by_title(pokemons, "Bulbizarre")
display(pokemons)

is_playing = True
while is_playing:
    print("********************")
    print("Bienvenue sur votre Pokedex")
    print("Options: \n1. Créer un pokemon\n2.Afficher\n3. Afficher les pokémons\n 4. Rechercher par nom")
    choix = input("Votre choix : ")
    if choix == "1":
        name = input("Name : ")
        numero = input("Numero : ")
        pokemon_type = input("Type : ")
        taille = input("Taille : ")
        poids = input("Poids : ")
        categorie = input("Catégorie : ")
        faiblesses = input("Faiblesses : ")
        talent = input("Talent :")
        sexe = input("Sexe : ")
        add_pokemon(name, numero, pokemon_type, taille, poids,
                    categorie, faiblesses, talent, sexe)
    elif choix == "2":
        print("1. Rechercher un pokémon par numéro\n2. Rechercher un pokémon par son nom")
        choix_2 = input("Votre choix :")
        if choix_2 == "1":

        display(pokemons)
