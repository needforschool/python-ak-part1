import random
import requests

class QuoteGenerator:
    def __init__(self):
        self.quotes = []
        
    def add(self, quote):
        self.quotes.append(quote)
        
    def random(self):
        return random.choice(self.quotes)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
generator = QuoteGenerator()

for quote in response.json():
    generator.add(quote["title"])

while True:
    input("Press any key to get a random quote:")
    print(generator.random())