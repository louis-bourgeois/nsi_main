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


def add_media(titre, type_, realisateur, annee, genre, acteurs):
    medias[titre] = {
        "type": type_,
        "realisateur": realisateur,
        "annee": annee,
        "genre": genre,
        "acteurs": acteurs
    }
