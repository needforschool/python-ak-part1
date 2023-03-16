import random
import requests

class QuoteGenerator:
    """
    Classe qui permet de générer des phrases aléatoires.
    """
    def __init__(self):
        """
        Constructeur de la classe QuoteGenerator.
        
        Initialise la liste des phrases vide.
        """
        self.quotes = []
        
    def add(self, quote: str):
        """
        Méthode permettant d'ajouter une nouvelle phrase à la liste des phrases.
        
        @param quote (str): La phrase à ajouter à la liste des phrases.
        """
        self.quotes.append(quote)
        
    def random(self):
        """
        Méthode permettant de générer une phrase aléatoire.
        
        @return (str): Une phrase aléatoire choisie parmi la liste des phrases.
        """
        return random.choice(self.quotes)

# Récupération des données depuis l'API
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# Génération d'un objet QuoteGenerator
generator = QuoteGenerator()

# Ajout des phrases de l'API à la liste des phrases
for quote in response.json():
    generator.add(quote["title"])

# Génération d'une phrase aléatoire et affichage dans la console à chaque appui sur une touche
while True:
    input("Press any key to get a random quote:")
    print(generator.random())