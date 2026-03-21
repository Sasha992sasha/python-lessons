class Employee:
    def __init__(self , name , position , salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_salary_info(self):
        print(f"Заробітна плата {self.name}: {self.salary}")

pracivnik = Employee("Саша" , "python_middle" , "50000") #число з голови я не помню сіки мідли заробляють
pracivnik.get_salary_info()