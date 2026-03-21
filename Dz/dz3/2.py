class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class Cart:
    def __init__(self):
        self.spisok = []

    def add(self , prod):
        self.spisok.append(prod)
    
    def remove(self,index):
        if  0 <= index < len(self.spisok):
            self.spisok.pop(index)
        else:
            print('Шось не то')
    
    def printer(self):
        for index, item in enumerate(self.spisok):
            print(f"{index}: {item.name} {item.count} штук")
  
    def totalPrice(self):
        total = 0
        for item in self.spisok:
            total+=item.price*item.count
        print (f"Загальна ціна {total}")

t1 = Product("Яблуко" , 20 , 1)
t2 = Product("Молоко" , 2 ,13)

cart = Cart()

cart.add (t1)
cart.add (t2)

cart.printer()

cart.totalPrice()