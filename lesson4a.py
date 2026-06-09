# class this is a blueprint/template that is used to create objects
# we create a class using a keyword class followed by the class name
# OOP- is a programming paradigm which combines variables/properties/characteristics/attributes and functions/methods/behaviour/action together for easy maintenance and management of code

# class simply wraps the functions and variables and you can access the functions and variables only through the object from that class.

class Farmer:
    # constructor- this is a special method that automatically runs whenever an object is created
    
    # its written using _init__()
    # self referes to the current object being created 

    def __init__(self):
        # attributes these are just variables that belong to an object 
        # they are usually written inside the constructor
        self.name="John"
        self.litres=50
    # methods- this is just a function inside a class they define what an object can do 
    # they use the self parameter to access the object attributes

    def display_info(self):
        print(f"Farmer Name: {self.name}")
        print(f"Milk delivered: {self.litres}")

# object is an instance of a class 
# so we need an object to acess the attributes and methods of the class
farmer1=Farmer()
# now using farmer1 object we can access attributes and methods in the Farmer class 
farmer1.display_info()
        

