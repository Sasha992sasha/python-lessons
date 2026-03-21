class Employee:
    def __init__(self,name,posada,zarplata):
        self.name = name
        self.posada = posada
        self.zarplata = zarplata

class Departament:
    def __init__(self):
        self.spisok = []

    def add(self,a):
        self.spisok.append(a)
    
    def remove(self , b):
        if 0 <= b <= len(self.spisok):
            self.spisok.pop(b)
        else:
            print("Шото не то")

    def suma(self):
        total = 0
        for i in self.spisok:
            total+= i.zarplata
        print(total)

    def debug(self):
        for i in self.spisok:
            print(f"{i.name} | {i.posada} | {i.zarplata}") #дуже вдобно 1 раз написав і все провірив

a1=Employee('Саша' , "back-end" , 1)

a2=Employee('Саша-aльтр его' , "front-end" , 2)

a3=Employee('Даня' , "Далекобійник" , 3)

dep = Departament()

dep.add(a1)
dep.add(a2)
dep.add(a3)

dep.debug() #це я зробив шоби провірить чи все робе та й оставив вдруг пригодиться

dep.suma()

dep.remove(1)

dep.suma()

dep.debug()
