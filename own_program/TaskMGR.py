import colorama , datetime , re

class Task:
    def __init__(self,name,dedline,deskr):
        self.name = name
        self.dedline = dedline
        self.deskr = deskr

class TaskMGR:
    def __init__(self):
        self.tasks = []
        try:
            with open("task.txt", "r", encoding="utf-8") as f:
                for i in f:
                    i = i.strip()
                    name,dedline,deskr = i.strip().split(' | ')
                    self.tasks.append(Task(name,dedline,deskr))
        except :
            print("Шось не те з файлом")
            a = open("task.txt" , "w" , encoding="utf-8")
    
    def save_file(self):
        with open("task.txt", "w", encoding="utf-8") as f:
            for i in self.tasks:
                f.write(f"{i.name} | {i.dedline} | {i.deskr} \n")
    
    def add(self,file):
        self.tasks.append(file)

    def remov(self,index):
        try:
            self.tasks.pop(index)
        except IndexError:
            input('Не той індекс')

    def print_task(self):
        today = datetime.date.today()
        for index , i in enumerate(self.tasks):  
            try:
                normalDedline = datetime.datetime.strptime(f"{i.dedline}.{today.year}", "%d.%m.%Y").date()
                t = (normalDedline - today).days
                if t <= 0:
                    color = colorama.Fore.RED
                elif t <= 3:
                    color = colorama.Fore.YELLOW
                else:
                    color = colorama.Fore.GREEN
            except:
                color = ""
            print(f"{color}{index}: {i.name} | {i.dedline} | {i.deskr}{colorama.Style.RESET_ALL}")
            
def save_prin():
    MGR.save_file()
    MGR.print_task()
    input()

MGR = TaskMGR()

MGR.print_task()

a = input('1-додати 2-прибрать ')

if a == "1":
    b = input("Введи назву ") 
    c = input("Введи дедлайн ") 
    d = input("Введи опис ")
    e = Task(b,c,d)
    MGR.add(e)
    save_prin()
    
elif a == "2":
    f = int(input("Введи id "))
    MGR.remov(f)
    save_prin()

elif a not in ("1", "2"):
    mat = re.match(r"([^\+\d]+)\+(\d+)(.*)", a)
    b = mat.group(1).strip()
    try:
        h = int(mat.group(2))
    except:
        print('Шось не так')
    d = mat.group(3) if mat.group(3) else "-"
    c = datetime.date.today() + datetime.timedelta(days=h)
    c = c.strftime("%d.%m")
    e = Task(b,c,d)
    MGR.add(e)
    save_prin()
    