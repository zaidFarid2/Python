# class BankAccount:
#     def UserInfo(self):
#         self.balance = 5000
#         userName = "w"
#         password = 1
#         self.name = input("Enter Your Username : ")
#         self.password = int(input("Enter Your Password : "))
#         if userName == self.name and password == self.password:
#             ask = input("Do you want Deposit or Withdraw : ")
#             if ask == "Withdraw":
#                 withdraw_info = self.withdraw()
#                 return f"Username: {self.name}\nPassword: {self.password}\n{withdraw_info}\nBalance: {self.balance}"
#             else:
#                 deposit_info = self.deposit()
#                 return f"Username: {self.name}\nPassword: {self.password}\n{deposit_info}\nBalance: {self.balance}"
#         else:
#             return "Invalid Password"
        
#     def deposit(self):
#         self.amount = int(input("Enter Deposit Amount : "))
#         self.balance += self.amount
#         return f"Your Deposit Amount Is : {self.amount} and Your Current balance Is {self.balance}"
        
#     def withdraw(self):
#         self.amount = int(input("Enter Withdraw Amount  : "))
#         if self.amount > self.balance:
#             return "Insufficient Balance"
#         else:
#             self.balance -= self.amount
#             return f"Your Withdraw Amount Is {self.amount} and Your Current Balance Is {self.balance}"

# # Example usage
# account = BankAccount()
# output = account.UserInfo()  # Get the output from UserInfo()

# with open("example.txt", "w") as file:
#     file.write(output)  # Write the output to the file