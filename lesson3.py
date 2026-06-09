def login():
    mypin = "8989"
    trials = 3

    while trials > 0:
        pin = input("Enter your PIN: ")

        if pin == mypin:
            print("\nLogin successful ")
            return True

        trials -= 1
        print("Wrong PIN ")

        if trials > 0:
            print("Attempts left:", trials)

    return False


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful ")
    else:
        print("Insufficient funds ")

    return balance


balance = 9000

if login():

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is Ksh", balance)

        elif choice == "2":
            balance = deposit(balance)
            print("New balance:", balance)

        elif choice == "3":
            balance = withdraw(balance)
            print("New balance:", balance)

        elif choice == "4":
            print("Thank you")
            break

        else:
            print("Invalid choice ")

else:
    print("Account locked ")
