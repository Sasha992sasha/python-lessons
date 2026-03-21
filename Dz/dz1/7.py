a = int(input("Скільки балів "))

if 0 <= a <= 49:
    print("Незадовільно")
elif 50 <= a <= 69:
    print("Задовільно")
elif 70 <= a <= 89:
    print("Добре")
elif 90 <= a <= 100:
    print("Відмінно!")
else:
    print("Шось не так")