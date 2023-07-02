class Organism:
    alive=True

    def livemsg(self):
        print('Parent has been born')

class Animal(Organism):  # inherited from organism
    def think(self):
        print('Animal is thinking')

class Dog(Animal):  # inherited from animal class
    
    def eat(self):
        print('The child dog is barking')

doggy=Dog()
doggy.livemsg()
doggy.think()
doggy.eat()
