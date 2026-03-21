class Suma:
    def __init__(self):
        self.total = 0

    def add(self, num , extra):
        self.total += num 
        self.total += extra
        return self.total
        
#я надіюся воно має бути так

c = Suma()

print(c.add(1 , 5))
print(c.add(11 , 2))
print(c.add(5 , 2))
print(c.add(3 , 0))
print(c.add(2 , 11))