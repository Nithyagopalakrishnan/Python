class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Welcome to Bank service")
	def deposit(self):
		deposit=float(input("Enter the Amount to be Deposited: "))
		self.balance=self.balance+deposit
		print("Your balance is: ",self.balance)
	def withdraw(self):
		withdraw=int(input("Enter The Amount to be Withdraw: "))
		if (self.balance <= withdraw):
			print("Account balance is insufficient")
		else:
			print("You withdraw: ",withdraw)
			self.balance=self.balance-withdraw
			print("Remaining Balance is: ",self.balance)
	def display(self):
		print("account balance is: ",self.balance)
S=Bank_Account()
S.deposit()
S.withdraw()
S.display()
