def log(func):
    def wrapper():
        func(self,amount):
        file  = open("logs.txt","a+")
        file.write(f"Amount ")




class BankAccount:
    def __init__(self,name,password):
        self.name  = name 
        self.password  = password 
        # self.amount  = amount 
        self.balance = 0
        self.isAuthenticator = False

    def authenticate(self,name,password):
        if self.name == name and self.password == password:
            self.isAuthenticator = True
        else:
            self.isAuthenticator = False

    def deposite(self,depamount):
        self.depamount = depamount
        if self.isAuthenticator:
            self.balance += self.depamount
        else:
            print("jana")

    def withdraw(self,withamount):
        self.withamount = withamount
        if self.isAuthenticator:
            self.balance -= self.withamount
        else:
            print("jana")        


a1 = BankAccount("zaid",1235)
a1.deposite(40)
a1.withdraw(20)

