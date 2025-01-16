medias = {
    "Inception": {
        "type": "Film",
        "realisateur": "Christopher Nolan",
        "annee": 2010,
        "genre": "Science-Fiction",
        "acteurs": ["Leonardo DiCaprio", "Elliot Page", "Tom Hardy"]
    },
    "Breaking Bad": {
        "type": "Série",
        "realisateur": "Vince Gilligan",
        "annee": [2008, 2013],
        "genre": "Drame",
        "acteurs": ["Bryan Cranston", "Aaron Paul", "Anna Gunn"]
    },
    "Star Wars: Episode III": {
        "type": "Film",
        "realisateur": "George Lucas",
        "annee": 2005,
        "genre": "Science-Fiction",
        "acteurs": ["Ewan McGregor", "Natalie Portman", "Hayden Christensen"]
    },
    "Avengers: Endgame": {
        "type": "Film",
        "realisateur": "Anthony et Joe Russo",
        "annee": 2019,
        "genre": "Super-Héros",
        "acteurs": ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"]
    },
    "Django Unchained": {
        "type": "Film",
        "realisateur": "Quentin Tarantino",
        "annee": 2012,
        "genre": "Western",
        "acteurs": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio"]
    },
    "Game of Thrones": {
        "type": "Série",
        "realisateur": "David Benioff et D.B. Weiss",
        "annees": [2011, 2019],
        "genre": "Fantasy",
        "acteurs": ["Emilia Clarke", "Kit Harington", "Peter Dinklage"]
    }
}


def afficher_media(media):
    for titre, infos_media in media.items():
        print(f"***** {titre} *****")
        for data, data_value in infos_media.items():
            print(f"      - {data}: {data_value}")


def add_media(titre, type, realisateur, annee, genre, acteurs):
    medias[titre] = {
        "type": type,
        "realisateur": realisateur,
        "annee": annee,
        "genre": genre,
        "acteurs": acteurs
    }
    print("Média ajouté à la structure")


def search_by_title(medias, title):
    # return medias[title]
    # ou avec une boucle
    for media_title in medias.keys():
        if media_title == title:
            return media[title]

add_media("Vaiana 2 ", "Film", "Dana Ledoux", "2024",
          "Animation, Comédie familiale", ["The Rock", "L'acteur qui chante Vaiana"])
afficher_media(medias)
