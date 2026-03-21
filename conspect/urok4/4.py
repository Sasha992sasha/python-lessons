class Class1:
    def print(self):
        print("Hello")


class Class2(Class1):
    def print(self):
        print("world")
        super().print()


q = Class2()
q.print()
 