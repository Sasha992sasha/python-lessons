class Task:
    def __init__(self,name,dedline,deskr):
        self.name = name
        self.dedline = dedline
        self.deskr = deskr

class TaskMBR:
    def __init__(self):
        self.tasks = []
        try:
            with open("task.txt" , "r")as f:
                for i in f:
                    i = i.strip()
                    name,dedline,deskr = i.strip().split(' | ')
                    self.tasks.append(Task(name,dedline,deskr))
        except FileNotFoundError :
            print("Нема твоїх завдань(")
            a = open("task.txt" , "w")
    
    def save_file(self):
        with open ("task.txt" , 'w') as f:
            for i in self.tasks:
                f.write(f"{i.name} | {i.dedline} | {i.deskr} \n")
    
    def add(self,file):
        self.tasks.append(file)

    def remov(self,index):
        try:
            self.tasks.pop(index)
        except IndexError:
            input('В тебе пусто ')

    def print_task(self):
        for index , i in enumerate(self.tasks):  
            print(f"{index}: {i.name} | {i.dedline} | {i.deskr}")

MBR = TaskMBR()

MBR.print_task()

try:
    a = int(input('Введи дію 1-додати 2-прибрать '))
except ValueError:
    print("Пока")


if a == 1:
    b = input("Введи назву ")
    c = input("Введи дедлайн ")
    d = input("Введи опис ")
    e = Task(b,c,d)
    MBR.add(e)
    print("Ось список")
    MBR.print_task()
    MBR.save_file()
    input()
    
elif a == 2:
    f = int(input("Введи id "))
    MBR.remov(f)
    MBR.save_file()
    MBR.print_task()
