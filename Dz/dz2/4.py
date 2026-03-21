class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height
        
    def calculate_aera(self):
        print(self.width*self.height)
    def calculate_perimetr(self):
        print(self.width+self.height+self.width+self.height)

pramo = Rectangle(10 , 20)

q = int(input("Виберіть дію 1-площа 2-периметр "))
if q == 1:
    pramo.calculate_aera()
elif q== 2:
    pramo.calculate_perimetr()
