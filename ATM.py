class User:
    def __init__(self, id, pin, balance):
        self.id = id
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

class ATM:
    def __init__(self, users):
        self.users = users
        self.current_user = None

    def login(self):
        user_name = input("Enter ID: ")
        entered_pin = input("Enter PIN: ")

        for user in self.users:
            if user.id == user_name and user.verify_pin(entered_pin):
                self.current_user = user
                return True
        print("Invalid ID/PIN")
        return False

    def display_balance(self):
        if self.current_user:
            print("Balance is " + str(self.current_user.balance))
        else:
            print("Error")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.current_user.balance:
            print("Insufficient funds")
        else:
            self.current_user.balance -= amount
            print("Cash withdrawn")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.current_user.balance += amount
            print("Deposited")

    def run(self):
        while True:
            if not self.current_user:
                if not self.login():
                    continue

            print("\nMenu:")
            print("1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Quit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.display_balance()
            elif choice == '2':
                amount = float(input("Enteramount: "))
                self.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount: "))
                self.deposit(amount)
            elif choice == '4':
                print("EXIT")
                break


userid = input("Enter ID: ")
userpin = input("Enter PIN: ")
userbalance = float(input("Enter Initial Balance: "))
user1 = User(userid, userpin, userbalance)

atm = ATM([user1])
atm.run()
