import random
r1 = random.randint(0, 50)
print(r1)
r2 = random.randint(0, 50)
print(r2)
r = r1 + r2
print(r)
Li = 3

while True:
    answer = input("Введите число от 0 до 100: ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    if answer > r:
        Li = Li - 1
        if Li == 0:
            print("Вы проиграли!")
            break
        else:
            print(f"Загаданное число меньше, осталось {Li} попытки")
    elif answer < r:
        Li = Li - 1
        if Li == 0:
            print("Вы проиграли!")
            break
        else:
            print(f"Загаданное число больше, осталось {Li} попытки")
    else:
        print("Вы угадали!")
        break
