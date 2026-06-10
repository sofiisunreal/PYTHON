# inheritance - this allows a class to inherit attributes and methods from other classes
# for inheritance to happen we have a  parent/super class which is the class being inheriited from and the child/sub class which is inheriting 

# after the child class inherits it will have both the parents attributes and the methods also its own attributes and methods

# parent/super class 
class Person:
    # constructor
    def __init__(self,name):
        self.name=name
    # method to display information 
    def display_info(self):
        print(f"Name of person is: {self.name}")
    # child/sub class which in inheriting from the person class 
class Farmer(Person):
    # constructor 
    # parent constructor being called by the super function 
    def __init__(self,name,litres):
        super().__init__(name)
        # attribute specific to the farmer child class 
        self.litres=litres
    def display_milk(self):
        print(f"Farmer name: {self.name}")
        print(f"Milk Delivered: {self.litres}")
    # method overriding 
    # the child class inherits from the parent class but then implements the inherited function on its own way 
    def display_info(self):
        print(f"Farmer name: {self.name}")

# creating an object 
farmer1=Farmer("John",56)
farmer1.display_info()
# farmer1.display_milk()


        