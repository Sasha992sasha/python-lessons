try:
    a = open("1.txt" ,"r")
except FileNotFoundError:
    a = open("1.txt" ,"w")
    a.write('Test')


print(a.read())