class Account:
    def __init__(self,balance) -> None:
        self.balance = balance
    def verification(self,name,password):
        self.name = "name"
        self.password = "password"
        if(name  == "zaid" and password  == "abc123"):
            print("User Login successfully")
        else:
            print("Please enter  a valid Username or paasword ")
    def deposite(self,depAmount):
        self.depAmount = "depAmount"
        self.balance+= depAmount
        # print(self.balance)
        print(f"{depAmount}Rs Deposite successfully")  
        print(f"your current balance is Rs{self.balance}")  
    def withdraw(self,amount):
        self.amount = "amount"
        self.balance-= amount
        if(amount>self.balance):
            print(f"You have not Enough money to withdraw")  
            # print(f"your current balance is Rs ${self.balance}")  

        else:
            print(f"{amount}Rs withdraw successfully")  
            print(f"your current balance is Rs ${self.balance}")  



a1 = Account(0)
a1.verification("zaid","abc123")
print("\t")
a1.deposite(60000)
print("\t")
a1.withdraw(25000)
print("\t")
a1.deposite(25000)
print("\t")
a1.withdraw(5000)
