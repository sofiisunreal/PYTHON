class Employee:
    def __init__(self,name,hours,rate,bonus_rate):
        self.name=name
        self.hours=hours
        self.rate=rate
        self.bonus_rate=bonus_rate
    def salary(self):
        payment=self.hours*self.rate
        return payment


    def bonus(self):
        if self.hours>100:
           bonus= self.bonus_rate*self.salary()
           total=self.salary()+bonus
        else:
            total=self.salary()
        return total
       
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Hours: {self.hours}")
        print(f"Salary: {self.salary()}")
        print(f"Employee Bonus: {self.bonus()}")
        print(f"Bonus rate:{self.bonus_rate}")
   
employee1=Employee("John",100,500,5)
employee1.display_info()

employee2=Employee("Mary",200,500,5)
employee2.display_info()

    
        