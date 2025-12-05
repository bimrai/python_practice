# represents a hero and the universe they belong to.
class SuperHero:
    #initialiser
    def __init__(self, hero: str, universe: str) -> None:
        self.hero = hero
        self.universe = universe


# create a hero instance
spiderman: SuperHero = SuperHero(hero = 'Spider-Man', universe = 'Marvel')
batman: SuperHero = SuperHero(hero = 'Batman', universe = 'DC')
# display hero information
print(f'The hero {spiderman.hero}, is from the {spiderman.universe} universe.')
print(f'The hero {batman.hero}, is from the {batman.universe} universe.')