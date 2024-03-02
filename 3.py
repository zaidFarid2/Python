class BankAccount:
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance
    def deposite(self,depAmount):
        self.depAmount = depAmount 
        self.__balance += depAmount
        print(f"{depAmount}Rs deposite successful, newbalance is{self.__balance} ")
    def withdraw(self,withAmount):
        self.withAmount = withAmount 
        self.__balance -= withAmount
        if(withAmount<self.__balance):
            print(f"You have not Enough money to withdraw")  
            # print(f"your current balance is Rs ${self.balance}")  

        else:
            print(f"{withAmount}Rs withdraw successfully")  
            print(f"your current balance is Rs ${self.__balance}")
        # print(f"{withAmount}Rs deposite successful, newbalance is{self.__balance} ")
    def __showBalance(self):
        print(f"cuurrent balance is {self.__balance} ")



a1 = BankAccount("zaid",1000)
a1.deposite(2000)
a1.withdraw(2000)

# a1._BankAccount__showBalance()  # This will print the balance

