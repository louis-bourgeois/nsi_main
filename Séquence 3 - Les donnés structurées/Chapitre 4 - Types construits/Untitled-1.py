import requests

# URL de l'API AnkiConnect
anki_connect_url = 'http://localhost:8765'

# Nom du deck
deck_name = "Baccalauréat::Spécialités::NSI::Premier DS::Ce qu'il faut revoir"

# Liste des flashcards existantes
flashcards = [
    {
        "Front": "Euclide\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: IIIᵉ siècle av. J.-C.\n- **Ce qu'il a fait**:\n  - Auteur de \"Les Éléments\", premier livre de mathématiques\n  - A décrit l'algorithme d'Euclide pour l'arithmétique des nombres entiers"
    },
    {
        "Front": "Al-Khwârizmî\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: IXᵉ siècle\n- **Ce qu'il a fait**:\n  - A introduit le système de numérotation décimale en Occident\n  - Père de l'algèbre; son nom est à l'origine du mot \"algorithme\""
    },
    {
        "Front": "George Boole\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: XIXᵉ siècle\n- **Ce qu'il a fait**:\n  - A inventé l'algèbre booléenne reliant logique et mathématiques\n  - Son travail est à la base de la logique des ordinateurs"
    },
    {
        "Front": "John von Neumann\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: XXᵉ siècle\n- **Ce qu'il a fait**:\n  - A conceptualisé l'architecture de base des ordinateurs (architecture von Neumann)\n  - A défini les composantes essentielles: unité arithmétique et logique, unité de contrôle, mémoire, entrées/sorties"
    },
    {
        "Front": "Alan Turing\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: XXᵉ siècle\n- **Ce qu'il a fait**:\n  - A proposé la machine de Turing, formalisant la notion de calcul\n  - A décrypté la machine Enigma, aidant à la défaite des nazis\n  - Père de l'intelligence artificielle; a imaginé le test de Turing"
    },
    {
        "Front": "Richard Stallman\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: XXᵉ-XXIᵉ siècles\n- **Ce qu'il a fait**:\n  - Fondateur du mouvement du logiciel libre et du projet GNU\n  - Créateur de l'éditeur de texte Emacs"
    },
    {
        "Front": "Linus Torvalds\n- Siècle ?\n- Ce qu'il a fait ?",
        "Back": "- **Siècle**: XXᵉ-XXIᵉ siècles\n- **Ce qu'il a fait**:\n  - Créateur du système d'exploitation Linux\n  - Promoteur du développement collaboratif du logiciel libre"
    },
]

# Ajout des nouvelles flashcards concernant les opérations sur les listes et les méthodes du module random
additional_flashcards = [
    {
        "Front": "Ajoute dans la liste après le dernier élément l'élément `e` donné en paramètre",
        "Back": "`list.append(e)`"
    },
    {
        "Front": "Insère dans la liste à l'indice donné en premier argument l'élément donné en deuxième argument",
        "Back": "`list.insert(i, valeur)`"
    },
    {
        "Front": "Range dans l'ordre croissant les éléments de la liste (ordre décroissant si `reverse=True`)",
        "Back": "`list.sort()`"
    },
    {
        "Front": "Inverse l'ordre des éléments dans la liste",
        "Back": "`list.reverse()`"
    },
    {
        "Front": "Supprime un élément par l'index `i` passé en argument",
        "Back": "`list.pop(i)`"
    },
    {
        "Front": "Retire l'objet `e` passé en argument de la liste (seule la première occurrence est retirée)",
        "Back": "`list.remove(e)`"
    },
    {
        "Front": "Donne l'élément maximum de la liste",
        "Back": "`max(list)`"
    },
    {
        "Front": "Donne l'élément minimum de la liste",
        "Back": "`min(list)`"
    },
    {
        "Front": "Renvoie le nombre d'éléments dans un objet (par exemple une liste)",
        "Back": "`len(objet)`"
    },
    {
        "Front": "Renvoie l'indice de la première occurrence de l'élément `e` dans la liste",
        "Back": "`list.index(e)`"
    },
    {
        "Front": "Mélange les éléments de la liste aléatoirement",
        "Back": "`random.shuffle(sequence)`"
    },
    {
        "Front": "Renvoie une nouvelle liste contenant un échantillon aléatoire de `k` éléments de la séquence d'entrée",
        "Back": "`random.sample(sequence, k)`"
    },
    {
        "Front": "Renvoie un élément aléatoire de la séquence",
        "Back": "`random.choice(sequence)`"
    },
    {
        "Front": "Renvoie un entier aléatoire `N` tel que `a <= N <= b`",
        "Back": "`random.randint(a, b)`"
    },
]

# Combiner les deux listes de flashcards
flashcards.extend(additional_flashcards)

# Fonction pour envoyer une requête à AnkiConnect
def invoke(action, params=None):
    return requests.post(anki_connect_url, json={
        'action': action,
        'version': 6,
        'params': params
    }).json()

# Créer le deck s'il n'existe pas
def create_deck(deck_name):
    invoke('createDeck', {'deck': deck_name})

# Ajouter les flashcards
def add_flashcards(flashcards, deck_name):
    notes = []
    for card in flashcards:
        note = {
            "deckName": deck_name,
            "modelName": "Basic (and reversed card)",
            "fields": {
                "Front": card["Front"],
                "Back": card["Back"]
            },
            "options": {
                "allowDuplicate": False
            },
            "tags": []
        }
        notes.append(note)
    result = invoke('addNotes', {'notes': notes})
    if 'error' in result and result['error']:
        print("Erreur lors de l'ajout des notes :", result['error'])
    else:
        print("Les flashcards ont été ajoutées avec succès.")

# Exécution du script
if __name__ == "__main__":
    # Créer le deck
    create_deck(deck_name)
    # Ajouter les flashcards
    add_flashcards(flashcards, deck_name)
    print("Les flashcards ont été ajoutées dans le deck :", deck_name)
