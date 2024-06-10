class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount:.2f}")
            print(f"Deposit successful. New balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount:.2f}")
            print(f"Withdrawal successful. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Transfer to {recipient_account}: -{amount:.2f}")
            print(f"Transfer successful. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid transfer amount.")

    def transactions_history(self):
        if self.transactions:
            print("Transactions History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions recorded.")

    def get_balance(self):
        print(f"Your current balance: {self.balance:.2f}")

def main():
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    # Simulate login authentication
    if user_id == "user" and pin == "1234":
        print("Login successful.")
        atm = ATM(1000)  # Initialize ATM with starting balance

        while True:
            print("\nATM Menu:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Check Balance")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                atm.transactions_history()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '4':
                amount = float(input("Enter amount to transfer: "))
                recipient_account = input("Enter recipient account number: ")
                atm.transfer(amount, recipient_account)
            elif choice == '5':
                atm.get_balance()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice.")
    else:
        print("Incorrect user ID or PIN.")

if __name__ == "__main__":
    main()