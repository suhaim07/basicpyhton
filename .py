bal1 = input ("enter the balance: ")
class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

acc1 = Account(bal1, 12345)
print(acc1.balance)
print(acc1.account_no)