class BankApp:
    def __init__(self, balance=0):
        self.__balance=balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount>self.__balance:
            print('Insufficient Balance')
        else:
            self.__balance-=amount
            print('Withdrawn :', amount)

    def balance_enquiry(self):
        return self.__balance


mybank=BankApp()
mybank.deposit(500)
res=mybank.balance_enquiry()
print('YOUR BALANCE IS :', res)

mybank.withdraw(200)

res=mybank.balance_enquiry()
print('YOUR BALANCE IS :', res)
