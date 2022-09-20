import random
r1 = random.randint(0, 100)
print(r1)
r2 = random.randint(0, 100)
print(r2)
r = r1 + r2
print(r)

while True:
    answer = input("Введите число: ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    live = 3
    if answer > r:
        live = live - 1
        print("Загаданное число меньше")
    elif answer < r:
        live = live - 1
        print("Загаданное число больше")
    elif live = 0:
        print("Вы проиграли!")
        break
    else:
        print("Вы угадали!")
        break

