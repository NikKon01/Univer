d = {}

while True:
    print("Добро пожаловать! Введите команды:\n0 - завершить программу\n1 - добавить контакат\n2 - удалить контакт\n3 - просмотреть телефонную книгу\n4 - изменить номер телефона")
    commands = int(input())

    if (commands < 0) and (commands > 4):
        print("Неверно введена команда!")
        continue

    elif commands == 0:
        print("Завершение программы...")
        break

    elif commands == 1:
        def get_num():

            num = input("Введите номер телефона: ")
            num = num.replace(" ", "").replace("-", "")

            if (num[0] == "8") and (len(num) == 11):
                num = num.replace("8", "+7", 1)
            if (num[0] == "7") and (len(num) == 11):
                num = "+" + num
            if (num[0] == "9") and (len(num) == 10):
                num = "+7" + num
            if (len(num) == 12) and (num[1:].isdigit()):
                return(num)
            else:
                print("Неправильно набран номер!")
                return get_num()
        def get_name():
            name = input("Введите имя: ")
            name = name.title()
            return name

        d[get_name] = get_num

        c = input("Всё? y/n")
            if c == 'y':
                break




print(d)

