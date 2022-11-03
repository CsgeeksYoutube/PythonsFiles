class Bank():
    def __init__(self,balance):
        self.balance = balance
        
    @staticmethod
    def find_interest(loan_money,interest_rate):
        return loan_money * (1+ interest_rate)

    @classmethod
    def find_interest_classmethod(cls,loan_money):
        return loan_money*1.4

    def find_interest_instancemethod(self,loan_money):
        if self.balance <= 100:
            return loan_money*1.2
        else:
            return loan_money*1.5

class Atm(Bank):
    @staticmethod
    def find_interest(loan_money):
        return loan_money*1.3

atm=Atm(1000)
bank=Bank(50)
print(bank.find_interest(bank.balance,0.8))
print(bank.find_interest_classmethod(bank.balance))
print(bank.find_interest_instancemethod(bank.balance))
print(atm.find_interest(atm.balance))
print(Atm.find_interest_classmethod(atm.balance))
print(Atm.find_interest_instancemethod(bank,atm.balance))
print(Bank.find_interest_classmethod(atm.balance))
print(Bank.find_interest_classmethod(bank.balance))

