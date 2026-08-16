class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("Rs. ",amount, "was debited")

    def credit(self,amount):
        self.balance += amount
        print("Rs. ",amount,"was credited")
    def final(self):
        return self.balance

acc1 = Account(1000,1234)
acc1.debit(500)
acc1.credit(5000)
print(acc1.final())