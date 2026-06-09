# constructor with parameters 
class Farmer:
    def __init__(self,name,litres,price):
        self.name=name
        self.litres=litres
        self.price=price

    def calculated_payment(self):
        payment=self.litres*self.price
        return payment
    def display_info(self):
        print(f"Farmer name: {self.name}")
        print(f"Collected Litres: {self.litres}")
        print(f"Price per litre: {self.price}")
        print(f"Payment: Ksh{self.calculated_payment()}")

farmer1=Farmer("John",50,45)
farmer1.display_info()