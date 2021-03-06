"""
Коллекции (встроенные) в Python
* set() множества
* str() строки
* list() списки
* tuple() кортежи
* dict() словари
"""

"""
Множество - это неупорядоченная (неиндексируемая)
коллекция, способная хранить уникальные элементы разного типа. Множество - ссылочная коллекция.
"""

a_set = set([1,2,3])
b_set = a_set 
b_set.add(20000)
print("a_set:", a_set)
print("b_set:", b_set)


"""
Список - это упорядоченная (индексиуремая) коллекция,
способная хранить элементы разного типа. Список - ссылочная коллекция.
"""
num = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
num[2:5] = [200, 300, 400, 500]
print(num)

for n in num:
    print(n)
    num.append(n)
