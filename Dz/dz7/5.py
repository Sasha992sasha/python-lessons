class Suma:
    def __init__(self):
        self.total = 0

    def add(self, num):
        self.total += num
        return self.total
    
c = Suma()

print(c.add(1))
print(c.add(11))
print(c.add(5))
print(c.add(3))
print(c.add(2))