class Bank:
    def __init__(self):
        self.balance = 5000
        self.correctpin = "1234"
        self.trials = 3

class Account(Bank):
    def __init__(self):
        super().__init__(self,self.balance, self.correctpin, self.trials)

        # self.amount = amount
    def authentication (self):
        while self.trials > 0:
            pin = input("Enter your pin: ")

            if pin == self.correctpin:
                print("Welcome!")
                return  True
            else:
                self.trials -=1
                if self.trials > 0:
                    print("Wrong pin. Try again:")
                else:
                    print("Access Denied")
        return False

    def check_balance(self):
        print(f"Balance is {self.balance}")

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Withdrawal successful. New balance{self.balance}")
        else :
            print("Invalid Input")

    def withdraw (self,amount):
        if amount>0 and amount < self.balance :
            self.balance -= amount
            print(f"Withdrawal successful. New balance is {self.balance}")
        else :
            print("Invalid input.")

   
    
    def Menu (self):
        while True:
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("Enter option:")

            if choice == "1":
                self.check_balance ()
            elif choice == "2":
                amount = float(input("Enter your amount: "))
                self.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter your amount: "))
                self.deposit(amount)
            elif choice =="4":
                print("Thank you fo choosing us!")
                break

            else:
                print("Invalid input.")
atm = Account
if atm.authentication == True:
    atm.Menu()