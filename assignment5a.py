# area and perimeter 
class Shape:
    def __init__(self,name,length,width):
        self.name=name
        self.length=length
        self.width=width
    
class calculate(Shape):
    def __init__(self,name,length,width):
        super().__init__(name, length,width)
       
    def area(self):
        area= self.length * self.width
        return area
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        return perimeter

    def display_info(self):
        print(f"The area of the {self.name} is: {self.area()}")
        print(f"The perimeter of the {self.name} is :{self.perimeter()}")

rectangle=calculate("Rectangle",2,3)
rectangle.display_info()

square=calculate("Square",5,5)
square.display_info()