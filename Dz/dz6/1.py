a = {'саша': 14,
     'олєг': 13,
     'коля': 14}

try:
    b = int(input("Введи свій вік "))
except ValueError:
    print("Вік вводиться цифрами")
else:
    found = False

    for name, age in a.items():
        if age == b:
            found = True
            print("А ім'я не підкажеш?")
            c = input("Введи імя ").lower()

            if name == c:
                print("Та ти шо найшов")
            else:
                print("Шось імя в тебе не таке")

    if not found:
        print("Шось вік не підходящий")