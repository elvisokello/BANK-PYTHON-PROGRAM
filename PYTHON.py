class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Account Opening:", self.date_of_opening)
        print("Balance:", self.balance)
account = BankAccount("1234567890", 555000, "2023-01-31", "OKELLO ELVIS")
print("Amount deposited:", account.deposit(4000))
print("Amount withdrawn:", account.withdraw(8930))
account.check_balance()
account.customer_details()
