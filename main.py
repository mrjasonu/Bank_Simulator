
def login(name, account_no):
    with open('transactions.txt','w') as trans:
        real_account_no = "******" + str(account_no)[-3:]
        trans.write("-"*50)
        trans.write('\n'+"-"*50)
        trans.write(f"\n{name} just logged into his account and his account number is {real_account_no}.")

def make_transactions(to, amount):
    pass