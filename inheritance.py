# class Animal:

#     def eat(self):
#         print('Animal started eating')

#     def run(self):
#         print('Animal statrted running')
#     def sleep(self):
#         print('Animal strarted sleeping')

# class Rabbit(Animal):
#     pass
# class Parrot(Animal):
#     pass
# class Zebra(Animal):
#     pass

# rab=Rabbit()
# rab.eat()
class Animal:
    pass

    alive=True
    def eat(self):
        print('The animal is eating')
    def walk(self):
        print('The animal is walking')
    def sleep(self):
        print('The animal is sleeping')

class Rabbit(Animal):
    pass
class Dog(Animal):
    pass
class Mouse(Animal):
    pass

rabit=Rabbit()
rabit.walk()
