import random

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Account:
    def __init__(self, customer):
        self.customer = customer
        self.account_number = random.randint(10000, 99999)
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred ${amount} to account {recipient_account.account_number}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

class Transaction:
    @staticmethod
    def account_summary(account):
        print(f"Account Holder: {account.customer.name}")
        print(f"Account Number: {account.account_number}")
        print(f"Current Balance: ${account.balance}")

# Function to get user input for creating a customer
def get_customer_info():
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone = input("Enter customer phone number: ")
    return Customer(name, address, phone)

# Function to get user input for performing transactions
def perform_transactions(account):
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Account Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            recipient_account_number = input("Enter recipient's account number: ")
            amount = float(input("Enter amount to transfer: "))
            # In a real system, you would validate the recipient's account number
            # For simplicity, we assume the recipient account exists
            recipient_account = recipient_accounts.get(recipient_account_number)
            if recipient_account:
                account.transfer(amount, recipient_account)
            else:
                print("Recipient account not found")
        elif choice == '4':
            Transaction.account_summary(account)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# Example usage:

# Create customers
customer1 = get_customer_info()
customer2 = get_customer_info()

# Create accounts
account1 = Account(customer1)
account2 = Account(customer2)

# Mapping of account numbers to account objects for simplicity
recipient_accounts = {
    str(account2.account_number): account2,
    # Add more accounts here if needed
}

# Perform transactions for account1
perform_transactions(account1)
