class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("1233","siuu")
print(acc1.__acc_pass)