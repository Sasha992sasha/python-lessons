class BankAccount:
    def __init__(self, id_ac, name, balance):
        self.id_ac = id_ac
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
    
    def remove(self, account, grn):
        if account in self.accounts:
            if account.balance >= grn:
                account.balance -= grn
            else:
                print("Недостатньо коштів")
        else:
            print("Рахунок не знайдено")

    def perecaz(self, account1, account2, grn):
        if account1 in self.accounts and account2 in self.accounts:
            if account1.balance >= grn:
                account1.balance -= grn
                account2.balance += grn
                print(f"Баланс {account1.name} : {account1.balance}")
                print(f"Баланс {account2.name} : {account2.balance}")
            else:
                print('Недостатньо коштів')
        else:
            print("Рахунок не знайдено")
        
bank = Bank()

a1 = BankAccount(1, "Саша", 1000)
a2 = BankAccount(2, "Колясік", 1000)
a3 = BankAccount(3, "Йорик", 1000)
bank.add_account(a1)
bank.add_account(a2)
bank.add_account(a3)

bank.perecaz(a2, a3, 100)