class Car:

    airbag_count=2 # class object | it can be deleted also to check 
    
    def __init__(self,brand,color,model,tax):
        self.brand=brand      # object of constructor
        self.color=color
        self.model=model
        self.tax=tax
    
    def start_engine(self):
        print(f'The {self.brand} has started its engine and its color is {self.color}')
    def stop_engine(self):
        print(f'The {self.brand} has stopped its engine and its model was {self.model}')

mycar1=Car('Ford','Red','2022','Tax')
mycar2=Car('Toyota','Magenta','2023','cleared')

mycar1.airbag_count=3 # can be manipulated through class object | can be deleted also

print(mycar1.airbag_count)   
print(mycar2.airbag_count)
# can be changed through class itself also
Car.airbag_count=10
print(mycar1.airbag_count)
print(mycar2.airbag_count)

print(mycar1.brand,mycar1.color,mycar1.model,mycar1.tax,end="  ")
print(mycar2.brand,mycar2.color,mycar2.model,mycar2.tax,end="")

