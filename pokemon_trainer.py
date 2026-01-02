# Pokémon Trainer and Pokémon!

class Pokemon():
    def __init__(self, trainer, name, element, attack, speak):
        self.trainer = trainer
        self.name = name
        self.element = element
        self.attack = attack
        self.speak = speak
        
    def intro(self):
        return f'"Hello! I am {self.trainer} and my Pokémon is {self.name}! Say hi to {self.name}!'
        
    def pokemon_name(self):
        return f"Pokémon: {self.name}"
    
    def pikachu_speak(self):
        return f'{self.name}: "{self.speak}!"'
        
    def pokemon_type(self):
        return f'{self.name} is a {self.element} type Pokémon.'
    
    def pokemon_attack(self):
        return f'{self.trainer} chose {self.attack}. \n {self.trainer}: "{self.name}, use {self.attack}!'

pikachu = Pokemon('Bim', 'Pikachu', 'Electric', "Thunderbolt", "Pika Pika")

print(pikachu.intro())
print(pikachu.pokemon_name())
print(pikachu.pikachu_speak())
print(pikachu.pokemon_type())
print(pikachu.pokemon_attack())
