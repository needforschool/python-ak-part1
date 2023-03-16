import random

class QuoteGenerator:
    def __init__(self):
        self.quotes = []
        
    def add(self, quote):
        self.quotes.append(quote)
        
    def random(self):
        return random.choice(self.quotes)

# Phrases provenant de JSON Placeholder

generator = QuoteGenerator()
generator.add("sunt aut facere repellat provident occaecati excepturi optio reprehenderit")
generator.add("qui est esse")
generator.add("ea molestias quasi exercitationem repellat qui ipsa sit aut")
generator.add("eum et est occaecati")

print(generator.random())
