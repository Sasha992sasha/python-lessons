from random import randint

a = randint(1 , 10)
c = 3

while True:
    if c != 0:
        b= int(input("Введи число "))
        if b == a:
            print("Вгадав")
            break

        elif a<b:
            print("Число меньше")
            c -=1

        elif a>b:
            print("Число більше")  
            c -=1 

        else:
            print("Попробуй ше раз")
            
    else:
        print(f"Не вгадав число було {a}")
        break