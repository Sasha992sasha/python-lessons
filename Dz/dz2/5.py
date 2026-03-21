class Product:
    def __init__(self , name , price , quaniti):
        self.name = name
        self.price = price
        self.quaniti = quaniti
    def calculate_price(self):
        print(self.price*self.quaniti)
    def display_info(self):
        print(f'Назва {self.name} ціна {self.price} , кількість {self.quaniti}')

towar1 = Product("water" , 14 , 100)

q = int(input("Виберіть дію 1-ціна 2-інфо "))
if q == 1:
    towar1.calculate_price()
elif q== 2:
    towar1.display_info()