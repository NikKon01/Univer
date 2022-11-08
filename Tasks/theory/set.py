"Множества — это неупорядоченная коллекция уникальных элементов, сгруппированных под одним именем. Множество может быть неоднородным — включать элементы разных типов. Множество всегда состоит только из уникальных элементов (дубли запрещены) в отличие от списков и кортежей в Python. Объект set — это также коллекция уникальных хэшируемых объектов. Объект называется хэшируемым в том случае, если его значение хэша не меняется. Это используется в ключах словарей и элементах множеств, ведь значения хэшей применяются в их внутренних структурах. Чаще всего множества в Python используются для проверки на принадлежность, удаления повторов из последовательности и выполнения математических операций, таких как пересечение, объединение, поиск разностей и симметрических разностей. Изображение ниже показывает два примера множеств (алфавит и цифры), каждый из которых включает уникальные неизменяемые объекты."

a = set() # создаём пустое множество a

print(a)
print(type(a))

b = {} # используя пустые фигурные скобки по умолчанию создается словарь, не множество !
print(type(b))

b = {"self", 1, (1,2, 3)} # объявляем и инициализируем множество b. Способ 1
print(b)
print(type(b))

b = set(("self", 1, (1,2, 3))) # объявляем и инициализируем множество b. Способ 2
print(b)
print(type(b))

a.add(2) # добавление одного элемента во множество a
print(a)

a.update((3,4,5,6)) # добавление нескольких элементов во множество a
print(a)

# запрещено добавлять элементы изменяемых типов, такие как список или словарь

list_1 = [1,2,3]
dict = {"one": 1}

#a.add(list)
#print(a)

#a.add(dict)
#print(a)

# но с помощью функции set() можно преобразовать любой контейнер во множество

print(set(list_1))
print(set(dict))

# Удаление элементов из множества

set1 = {1, 2, 3, 4, 'a', 'p'}
print(set1)

set1.remove(2) #Метод remove() удаляет из множества конкретный элемент и возвращает ошибку в том случае, если его нет во множестве.
print(set1)
#set1.remove(5) # возникает ошибка


set1 = {1, 3, 4, 'a', 'p'}
print(set1)

set1.discard('a') # Метод discard() удаляет конкретный элемент и НЕ возвращает ошибку, если тот не был найден во множестве.
print(set1)

set1.discard(6)
print(set1) # ошибки не возникает


set1 = {1, 2, 3, 4}
set1.pop() #Метод pop() удаляет и возвращает по одному элементу за раз в случайном порядке. Set — это неупорядоченная коллекция, поэтому pop() не требует аргументов (индексов в этом случае). Метод pop() можно воспринимать как неконтролируемый способ удаления элементов по одному из множеств в Python.
a = set1.pop()
print(set1, a)


#Проверка вхождения объекта во множество

num_set = {1 ,3, 5, 7, 9, 10}
print(num_set)

print(7 in num_set)
print(1 not in num_set)


# Количество элементов во множестве num_set
print(len(num_set))

new_set = num_set.copy() # метод copy() — создает копию существующего множества и сохраняет ее в новом объекте.
print(len(new_set))

num_set.clear() # метод clear() —очищает множество (удаляет все элементы за раз)
print(num_set)

del num_set # del — удаляет множество целиком

#Операции множеств в Python

# Объединение множеств
#При использовании на двух множествах вы получаете новый объект, содержащий элементы обоих (без повторов). Операция объединения в Python выполняется двумя способам: с помощью символа | или метода union().

A = {1, 2, 3}
B = {2, 3, 4, 5}
C = A | B  # используя символьный метод
C = A.union(B) # используя метод union
print(C)

# Пересечение множеств
# При использовании на двух множествах вы получаете новый объект, содержащий общие элементы обоих (без повторов). Операция пересечения выполняется двумя способами: с помощью символа & или метода intersection().

A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A & B  # используя символьный метод
C = A.intersection(B)  # используя метод intersection
print(C)

# Разность множеств
#При использовании на двух множествах вы получаете новый объект, содержащий элементы, которые есть в первом, но не втором (в данном случае — в множестве “A”). Операция разности выполняется двумя способами: с помощью символа - или метода difference().

A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A - B # используя символьный метод
C = A.difference(B) # используя метод difference
print(C)

#Симметричная разность множеств
#При использовании на двух множествах вы получаете новый объект, содержащий все элементы, кроме тех, что есть в обоих. Симметрическая разность выполняется двумя способами: с помощью символа ^ или метода symmetric_difference().

C = A ^ B  # используя символьный метод
C = A.symmetric_difference(B)  # используя метод symmetric_difference
print(C)

#Подмножество и надмножество в Python
#Множество B (SetB) называется подмножеством множества A (SetA), если все элементы SetB есть в SetA. Проверить на подмножество в Python можно двумя способами: с помощью символа <= или метода issubset(). Он возвращает True или False в зависимости от результата.

A = {1, 2, 3, 4, 5}
B = {2,3,4}
print(B <= A)  # используя символьный метод
print(B.issubset(A)) # используя метод issubset

# Множество A (SetA) называется надмножеством множества B (SetB), если все элементы SetB есть в SetA. Проверить на надмножество в Python можно двумя способами: с помощью символа >= или метода issuperset(). Он возвращает True или False в зависимости от результата.

A = {1, 2, 3, 4, 5}
B = {2,3,4}
print(A >= B)  # используя символьный метод
print (A.issuperset(B)) # используя метод issubset

# Удаление дубликатов из списка путём преобразования его во множество и обратно

List1 = [1, 2, 3, 5, 3, 2, 4, 7]
print(List1)

List_without_duplicate = set(List1)
List1 = list(List_without_duplicate)
print(List1)

# В одну строку:

List1 = list(set(List1))
print(List1)