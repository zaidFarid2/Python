
def log(func):
    def wrapper(self, amount):
        func(self, amount)
        file = open("logs.txt", "a+")
        file.write(f"Amount {amount} {func.__name__} successfully\n")
        file.close()
    return wrapper

class BankAccount:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.balance = 0
        self.isAuthenticated = False

    def authenticate(self, userName, password):
        if self.userName == userName and self.password == password:
            self.isAuthenticated = True
        else:
            self.isAuthenticated = False
    
    @log
    def deposit(self, amount):
        if self.isAuthenticated:
            self.balance += amount
        else:
            print("Authentication failed.")
    
    @log
    def withdrawal(self, amount):
        if self.isAuthenticated:
            if amount < self.balance:
                self.balance -= amount
            else:
                print("Invalid Amount to withdraw.")
        else:
            print("Authentication failed.")

account = BankAccount("ali", "123")
account.authenticate("ali", "123")
account.deposit(100)
account.withdrawal(50)