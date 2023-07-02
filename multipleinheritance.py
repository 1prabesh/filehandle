class Prey:

    def fly(self):
        print('This fly')
    
class Predator:

    def hunt(self):
        print('This hunts')

class Rabbit(Prey):
    pass
class Eagle(Predator):
    pass

class Fish(Prey,Predator):
    pass

rab=Rabbit()
eag=Eagle()
fis=Fish()

rab.fly(), eag.hunt(),fis.hunt(),fis.fly()   # fish can access both class method while other two can have their only parent class
