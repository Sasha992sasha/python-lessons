class Task:
    def __init__(self, name, opis, dedline):
        self.name = name
        self.opis = opis
        self.dedline = dedline
        self.stan = False

class Taskmgr:
    def __init__(self):
        self.taskList = []

    def add_task(self, task):
        self.taskList.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.taskList):
            self.taskList.pop(index)

    def mark(self, index):
        if 0 <= index < len(self.taskList):
            self.taskList[index].stan = True

    def show(self):
        for i, task in enumerate(self.taskList):
            status = "Done" if task.stan else "Not done"
            print(f"{i}. {task.name} | {task.opis} | {task.dedline} | {status}")

zav = Task('Дз' , 'Біологія' , '7.03.26')
zav1 = Task('Музика' , "Написать акордові послідовності" , "10.03.26")

manager = Taskmgr()

manager.add_task (zav)
manager.add_task (zav1)

manager.mark(1)

manager.show()