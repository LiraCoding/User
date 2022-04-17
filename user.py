class User:		# here's what we have so far
    def __init__(self, int_rate=0.04, balance=0): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount 
        print(self.balance)
        return self   

    def display_account_info(self):
        print("The remaining balance is:", self.balance)
        return self

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("insufficient funds:Charging fee=$10.00")
        else:
            self.balance -= amount
        print("The remaining balance is:", self.balance)
        return self





pete_bank_account = User(2600, 0.02)
max_bank_account = User(13000, 0.01)
luke_bank_account = User(1000, 0.04)


pete_bank_account.deposit(500).deposit(2000).deposit(5000).withdraw(9000).display_account_info()
print("Pete's balance is:", pete_bank_account.balance)

max_bank_account.deposit(500).deposit(500).withdraw(430).withdraw(100).withdraw(150).display_account_info()
print("Max's balance is:", max_bank_account.balance)

luke_bank_account.deposit(500).withdraw(430).withdraw(100).withdraw(150).display_account_info()
print("luke's balance is:", luke_bank_account.balance)
