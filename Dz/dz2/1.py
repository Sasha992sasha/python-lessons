class BankAccount:
    def __init__(self , account_number , balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self):
        a = int(input("Скільки додати "))
        self.balance += a
        print(f"Баланс {self.balance}")

    def whithdraw(self):
        b = int(input("Скільки зняти "))
        if self.balance >= b:
            self.balance-=b
            print(f"Операція виконана баланс {self.balance}")
        else:
            print("Недостатно коштів")
    def balanceShow(self):
        print(f"Ваш баланс {self.balance}")
        
        
user = BankAccount(1 , 100)
q = int(input("Виберіть дію 1-додати гроші 2-відняти 3-показати баланс "))
if q == 1:
    user.deposit()
elif q== 2:
    user.whithdraw()
elif q == 3:
    user.balanceShow()