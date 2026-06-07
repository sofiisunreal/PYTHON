# while loop-  executes a block of code a number of times based on a condition
# initialize
# while condition:
#      block of code
#      increment/decreament

counter=1
while counter<=5:
     print(f"Hello {counter}")
     counter+=1

mypin = "8989"
trials = 3
balance = 9000

while trials > 0:
    pin = input("Enter your Pin: ")

    if pin == mypin:
        print("Login successful ")

        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("You have Ksh", balance, "in your account")

            elif choice == "2":
                add = float(input("Enter amount: "))
                balance += add
                print("You now have Ksh", balance)

            elif choice == "3":
                remove = float(input("Enter amount to withdraw: "))

                if remove <= balance:
                    balance -= remove
                    print("You now have Ksh", balance)
                else:
                    print("Insufficient funds")

            elif choice == "4":
                print("Thank you for using our services")
                break

            else:
                print("Invalid Choice")

        break

    else:
        trials -= 1
        print("Wrong Pin.")

        if trials > 0:
            print("You have", trials, "trials remaining")
        else:
            print("Account locked")
