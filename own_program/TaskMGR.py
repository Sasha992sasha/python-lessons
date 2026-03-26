import colorama , datetime , re

colorama.init()

class Task: #це клас для завдань
    def __init__(self,name,dl,dsk):
        self.name = name
        self.dl = dl
        self.dsk = dsk

class TaskMGR: #це основа робота планувальника
    def __init__(self):
        self.tasks = []
        try:
            with open("task.txt", "r", encoding="utf-8") as f: #це відкриття файлу
                for i in f:
                    i = i.strip()
                    name,dl,dsk = i.strip().split(' | ')
                    self.tasks.append(Task(name,dl,dsk))
        except :
            print("Шось не те з файлом")
            with open("task.txt" , "w" , encoding="utf-8"): # це створення + заміна
                pass
    
    def save_file(self): # це зберігання файлу
        with open("task.txt", "w", encoding="utf-8") as f:
            for i in self.tasks:
                f.write(f"{i.name} | {i.dl} | {i.dsk} \n") 
    
    def add(self,file): # це додавання завдання в список з якого воно попадає в файл
        self.tasks.append(file)

    def remov(self,index): #це видалення з списку
        try:
            self.tasks.pop(index)
        except IndexError:
            input('Не той індекс')

    def print_task(self): #це вивід
        today = datetime.date.today()
        for index , i in enumerate(self.tasks):  
            try:
                normaldate = datetime.datetime.strptime(f"{i.dl}.{today.year}", "%d.%m.%Y").date()
                t = (normaldate - today).days #це 'Дельта дат'
                if t <= 0:
                    color = colorama.Fore.RED # це кольори
                elif t <= 3:
                    color = colorama.Fore.YELLOW
                else:
                    color = colorama.Fore.GREEN
            except:
                color = ""
            print(f"{color}{index}: {i.name} | {i.dl} | {i.dsk}{colorama.Style.RESET_ALL}") #це сам вивід з форматуванням
            
def save_prin(): #це вдобна команда щоби не повторюватись по 100 раз
    MGR.save_file()
    MGR.print_task()
    input()

MGR = TaskMGR()

MGR.print_task() #це вивід

a = input('1-додати 2-прибрать ')

if a == "1":
    b = input("Введи назву ") 
    c = input("Введи дедлайн ")
    d = input("Введи опис ")
    
    if c.startswith('+'):#швидка дата просто +1 замість 23.03
        try:
            days = int(c.removeprefix('+'))
            c = datetime.date.today() + datetime.timedelta(days=days)    
            c = c.strftime("%d.%m")
        except:
            input("Щось не так з +датою ")
            
    e = Task(b,c,d)
    MGR.add(e)
    save_prin()
    
elif a == "2":
    f = int(input("Введи id "))
    MGR.remov(f)
    save_prin()

elif not a.isdigit(): #це швидкий набір по типу Name+1description
    mat = re.match(r"([^\+\d]+)\+(\d+)(.*)", a)
    if not mat:
        print("Шось не то")
        input()
    else:
        b = mat.group(1).strip()
    try:
        h = int(mat.group(2)) #дедлайн
    except:
        print('Шось не так')# зроблено погано але ним ніхто не користується тому всеодно
    d = mat.group(3) if mat.group(3) else "-"
    c = datetime.date.today() + datetime.timedelta(days=h) 
    c = c.strftime("%d.%m") # це форматування
    e = Task(b,c,d)
    MGR.add(e)
    save_prin()
    