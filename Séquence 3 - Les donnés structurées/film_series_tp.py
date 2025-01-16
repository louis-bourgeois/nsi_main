medias = {
    "Inception": {
        "type": "Film",
        "réalisateur": "Christopher Nolan",
        "année": 2010,
        "genre": "Science-Fiction",
        "acteurs": ["Leonardo DiCaprio", "Elliot Page", "Tom Hardy"]
    },
    "Breaking Bad": {
        "type": "Série",
        "créateur": "Vince Gilligan",
        "années": [2008, 2013],
        "genre": "Drame",
        "acteurs": ["Bryan Cranston", "Aaron Paul", "Anna Gunn"]
    },
    "Star Wars: Episode III": {
        "type": "Film",
        "réalisateur": "George Lucas",
        "année": 2005,
        "genre": "Science-Fiction",
        "acteurs": ["Ewan McGregor", "Natalie Portman", "Hayden Christensen"]
    },
    "Avengers: Endgame": {
        "type": "Film",
        "réalisateur": "Anthony et Joe Russo",
        "année": 2019,
        "genre": "Super-Héros",
        "acteurs": ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"]
    },
    "Django Unchained": {
        "type": "Film",
        "réalisateur": "Quentin Tarantino",
        "année": 2012,
        "genre": "Western",
        "acteurs": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio"]
    },
    "Game of Thrones": {
        "type": "Série",
        "créateur": "David Benioff et D.B. Weiss",
        "années": [2011, 2019],
        "genre": "Fantasy",
        "acteurs": ["Emilia Clarke", "Kit Harington", "Peter Dinklage"]
    }
}


def ajouter_media(medias, nom, type_media, realisateur, annee, genre, acteurs):
    medias[nom] = {
        "type": type_media,
        "réalisateur" if type_media == "Film" else "créateur": realisateur,
        "année" if type_media == "Film" else "années": annee,
        "genre": genre,
        "acteurs": acteurs
    }
