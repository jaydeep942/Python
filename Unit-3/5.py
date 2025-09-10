# Create a Bank class with two variables Name and Balance. Implement
# a constructor to initialize the variable. Also implement deposit and
# withdrawal using instance methods.


class Bank:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withDrawal(self,amount):
        if amount > self.balance:
            print("Your balance is not to withdraw this amount.")
        else: 
            self.balance -=amount
            print(f"withdraw amount {amount}. New balance is {self.balance}.")
    
    def display(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")


print("\n=========== First value without any deposit and withdrawal ===========\n")
bank_abc = Bank("Shashwat",300000)
bank_abc.display()


print("\n=========== First value with deposit ===========\n")
bank_abc.deposit(50000)
# bank_abc.display()

print("\n=========== First value with withdrawal ===========\n")
bank_abc.withDrawal(100000)
# bank_abc.display()

