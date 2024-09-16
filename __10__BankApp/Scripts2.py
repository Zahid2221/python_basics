class BankApp:
    def __init__(self, balance=0):
        self.__balance=balance

    def deposit(self, amount):
        self.__balance += amount
        print('Successfully deposited ', amount)
    def withdraw(self, amount):
        if amount>self.__balance:
            print('Insufficient Balance')
        else:
            self.__balance-=amount
            print('Withdrawn :', amount)

    def balance_enquiry(self):
        return self.__balance

mybank=BankApp()

while True:
    n=int(input('Enter 1.Continue 2.Cancel :'))
    if n==1:
        x=int(input('Enter 1.Deposit 2.Withdraw 3.Balnace Enquiry 4.Cancel :'))
        if x==1:
            amount=int(input('Enter amount to deposit :'))
            mybank.deposit(amount)
        elif x==2:
            amount=int(input('Enter amount to withdraw :'))
            mybank.withdraw(amount)
        elif x==3:
            res=mybank.balance_enquiry()
            print('Your Account Balance is :', res)
        elif x==4:
            print('Thankyou for your Time')
        else:
            print('Invalid Input')
    elif n==2:
        print('Thankyou Visit Again')
    else:
        print('Invalid Input')


