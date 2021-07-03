
def login(name, account_no):
    with open('transactions.txt','a') as trans:
        real_account_no = "******" + str(account_no)[-3:]
        trans.write('\n'+"-"*50)
        trans.write('\n'+"-"*50)
        trans.write(f"\n{name} just logged into his account and his account number is {real_account_no}.")
    return name

def send_money(to, amount):
    balance_txt0 = open('balance.txt', 'r')
    balance = balance_txt0.read()
    new_balance= int(balance) - int(amount)
    balance_txt1 = open('balance.txt', 'w')
    balance_txt1.write(str(new_balance))
    transaction_txt = open('transactions.txt', 'a')
    transaction_txt.write("\n" + "-"*50)
    transaction_txt.write("\n" + "-"*50)
    transaction_txt.write(f"\n{name} sent a sum of ${amount} to {to}")#Date to be added later

def borrow_money(amount, collateral="House"):
    balance_txt = open('balance.txt')
    balance = int(balance_txt.read())
    new_balance=balance+int(amount)
    balance_txt.close()
    balance_txt = open('balance.txt', 'w')
    balance_txt.write(str(new_balance))
    balance_txt.close()
    trans_txt = open('transactions.txt', 'a')
    trans_txt.write("\n"+"-"*50)
    trans_txt.write("\n"+"-"*50)
    trans_txt.write(f"\n{name} borrowed a sum of ${str(amount)} from the bank. This person's new account balance is {str(new_balance)}")
    trans_txt.write(f"\n{name} used {collateral} as collateral.")
    trans_txt.close()

def check_balance():
    bal =  open('balance.txt')
    balance = bal.read()
    print(f"Your account balance is ${balance}.")
    bal.close()
    with open('transactions.txt', 'a') as trans:
        trans.write("\n"+"-"*50)
        trans.write("\n"+"-"*50)
        trans.write(f"\n{name} just checked his account balance and it was ${balance}.")

def start(user_input):
    if user_input == str(1) or user_input == "CHECK ACCOUNT BALANCE":
        print("\nWELCOME TO E-BANK CHECK BALANCE!")
        check_balance()
    elif user_input == str(2) or user_input == "SEND MONEY":
        print("\nWELCOME TO E-BANK SEND MONEY!")
        to = input("Whom would you like to send money to? ")
        amount = input("Amount: ")
        send_money(to, amount)
    elif user_input == str(3) or user_input == "BORROW MONEY":
        print("\nWELCOME TO E-BANK BORROW!")
        amount = input("How much would you like to borrow: ")
        collateral = input("What would you like to use as collateral: ")
        if collateral == "":
            borrow_money(amount)
        else:
            borrow_money(amount, collateral)


print("Welcome to E-Bank")

name = str(input("\nName: "))
acc_no = str(input("Account Number: "))
login(name, acc_no)

print(
"""
1.CHECK ACCOUNT BALANCE
2.SEND MONEY
3.BORROW MONEY
""")


run = 0
while run == 0:
    user_input = input("WHAT WOULD YOU LIKE TO DO? ")
    if user_input not in ["1","2","3"] and user_input not in ["CHECK ACCOUNT BALANCE", "SEND MONEY", "BORROW MONEY"]:
        run = 1
    else:
        start(user_input)
else:
    print("GOODBYE!")
