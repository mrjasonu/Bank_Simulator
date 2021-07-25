from datetime import datetime
class User:
    
    def __init__(self, name, account_no, account_balance):
        self.name = name.upper()
        self.account_no = account_no
        self.account_balance = account_balance
        self.now = datetime.now()
        with open('transactions.txt','a') as trans:
            fake_account_no = "******" + str(account_no)[-3:]
            trans.write('\n'+"-"*50)
            trans.write('\n'+"-"*50)
            trans.write(f"\n{name} just logged into his account and his account number is {fake_account_no}. Time: {self.now.strftime('%H:%M:%S, %d/%m//%y')}")

    def send_money(self, to, amount):
        balance_txt0 = open(self.account_balance, 'r')
        balance = balance_txt0.read()
        new_balance= int(balance) - int(amount)
        balance_txt1 = open(self.account_balance, 'w')
        balance_txt1.write(str(new_balance))
        transaction_txt = open('transactions.txt', 'a')
        transaction_txt.write("\n" + "-"*50)
        transaction_txt.write("\n" + "-"*50)
        transaction_txt.write(f"\n{self.name} sent a sum of ${amount} to {to.name}. Time: {self.now.strftime('%H:%M:%S, %d/%m//%y')}")
        to_account_balance = open(to.account_balance, 'r')
        new_to_account_balance = int(to_account_balance.read())+int(amount)
        to_account_balance.close()
        to_account_balance = open(to.account_balance, 'w')
        to_account_balance.write(str(new_to_account_balance))
        to_account_balance.close()

    def borrow_money(self, amount, collateral="House"):
        balance_txt = open(self.account_balance)
        balance = int(balance_txt.read())
        new_balance=balance+int(amount)
        balance_txt.close()
        balance_txt = open(self.account_balance, 'w')
        balance_txt.write(str(new_balance))
        balance_txt.close()
        trans_txt = open('transactions.txt', 'a')
        trans_txt.write("\n"+"-"*50)
        trans_txt.write("\n"+"-"*50)
        trans_txt.write(f"\n{self.name} borrowed a sum of ${str(amount)} from the bank. This person's new account balance is {str(new_balance)}")
        trans_txt.write(f"\n{self.name} used {collateral} as collateral. Time: {self.now.strftime('%H:%M:%S, %d/%m//%y')}")
        trans_txt.close()
    
    def check_balance(self):
        bal =  open(self.account_balance)
        balance = bal.read()
        print(f"Your account balance is ${balance}.")
        bal.close()
        with open('transactions.txt', 'a') as trans:
            trans.write("\n"+"-"*50)
            trans.write("\n"+"-"*50)
            trans.write(f"\n{self.name} just checked his account balance and it was ${balance}. Time: {self.now.strftime('%H:%M:%S, %d/%m//%y')}")

user1 = User('Jim', 349543, 'balance1.txt')
user1 = User('Jack', 943222, 'balance1.txt')
