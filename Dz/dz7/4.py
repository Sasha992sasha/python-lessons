from random import choice

a = 'abcdefghijklmnopqrstuvwxyz'

def rand(cont):
    for q in range(cont):
        yield choice(a)

for i in rand(5):
    print(i)