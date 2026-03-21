try:
    a = input("Введи число: ")
    b = int(a)
    print(a)

except ValueError:
    print("Треба було вводить тіки число")