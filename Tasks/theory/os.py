"""
Что такое модуль os?
Модуль os в Python — это библиотека функций для работы с операционной системой. Методы, включенные в неё позволяют определять тип операционной системы, получать доступ к переменным окружения, управлять директориями и файлами:
проверка существования объекта по заданному пути;
определение размера в байтах;
удаление;
переименование и др.
"""

import os

print(os.name) # Определение типа ОС


# Изменение рабочей директории
# По умолчанию рабочей директорией программы является каталог, где содержится запускаемый модуль.
# Благодаря этому, можно не указывать абсолютный путь к файлу, если тот находится именно в этой папке.

os.getcwd() # Возвращает текущую рабочую директорию

print(os.getcwd())

os.chdir(r"/var/www/html") # Смена рабочей директории на ту, что указана в скобках

print(os.getcwd())



# Проверки на корректность

print(os.path.exists(r"C:\test.txt")) # Метод exists служит для проверки указанного пути. Возвращает True или False

print(os.path.isfile(r"C:\test.txt")) # Метод isfile проверяет, является ли определенный объект файлом. Возвращает True или False

print(os.path.isdir(r"C:\test.txt")) # Метод isdir проверяет, является ли определенный объект папкой. Возвращает True или False


# Создание директорий

os.mkdir(r"C:\new") # метод mkdir создает каталог (папку) new в корне диска C (mkdir может создать только одну папку!)

os.makedirs(r"C:\folder\first\second\third") # метод makedirs создает цепочку из каталогов, в данном случае в каталоге folder создана папка first, внутри папки first, создана папка second, внутри папки second, создана папка third


# Удаление файлов и директорий

os.remove(r"C:\test.txt") # метод remove служит для удаления одиночного файла

os.rmdir(r"C:\folder") # метод rmdir - удаляет одну пустую папку. При попытке удалить папку с данными возникнет ошибка

os.removedirs(r"C:\folder\first\second\third") # метод removedirs - удаляет несколько,вложенных друг в друга, пустых папок


# Переименование

os.rename(r"C:\folder", r"C:\catalog") # метод rename принимает на вход полный путь к объекту до переименования и полный путь к объекту после (с уазанием нового имени, вместо предыдущего)

os.renames(r"C:\folder\first\second", r"C:\catalog\one\two") # аналогичен предыдущему, но позволяет сразу переименовать целую цепочку объектов

print(os.path.getsize("D:\\test.txt")) # Возвращает размер объекта в байтах



# Запуск на исполнение

os.startfile(r"C:\test.txt") # метод startfile - эмулирует открытие/запуск файла



# Получение имени файла и директории

print(os.path.basename("C:/test.txt")) # метод os.path.basename возвращает имя файла с расширением, получая на вход полное имя к файлу

print(os.path.dirname("C:/folder/test.txt")) # метод os.path.dirname возвращает имя папки, получая на вход полное имя к файлу

print(os.listdir(r"C:\folder")) # метод listdir возвращает список имён объектов (файлов и папок), которые находятся по указанному адресу

print(os.path.split(r"C:\folder\test.txt")) # метод split разделяет полный путь к файлу, состоящий из каталогов и имя файла с расширением на две строки

print(os.path.join(r"C:\folder", "test.txt")) # метод join собирает полный путь к файлу из каталогов и имени файла с расширением