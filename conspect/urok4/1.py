class Human:
    price = 1000


class Student(Human):
    pass


class Teacher(Human):
    price = 500


sasha = Student()
anna = Teacher()

print(sasha.price)
print(anna.price)