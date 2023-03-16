import random

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

# Génération d'un objet QuoteGenerator
generator = QuoteGenerator()

# Ajout de quelques phrases à la liste des phrases
generator.add("sunt aut facere repellat provident occaecati excepturi optio reprehenderit")
generator.add("qui est esse")
generator.add("ea molestias quasi exercitationem repellat qui ipsa sit aut")
generator.add("eum et est occaecati")

# Génération d'une phrase aléatoire et affichage dans la console
print(generator.random())
