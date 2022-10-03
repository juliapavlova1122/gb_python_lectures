# функции продолжение

# # import lecture_1_function  # обращаемся к файлу lecture_1_function
# # print(lecture_1_function.f(1))

# import lecture_1_function as l # сокращаем название для удобства, по прежнему работает код из указанного файла
# print(l.f(1))
#-------------------
# def new_string(symbol, count): # функция new_string принимает 
# # в качестве аргумента некоторый символ и некоторое число
#     return symbol * count # возвращаем

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # ошибка
#----------------
# def new_string(symbol, count = 3): # count  делаем равным 3
#     return symbol * count 

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!! - использовали заданную 3 по умолчанию
# print(new_string(4)) # 12 - умножили symbol * count
#------------------------------
# возможность передачи енограниченного количества аргументов
# при ее описании перед аргументом ставим *

def concatenatio(*params):
    res: str = ""  # логика работы со строкой, цифры выдадут ошибку
    for item in params:
        res += item # склеивание строк
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1

# c цифрами
def concatenatio(*params):
    res: int = 0 # работа с цифрами, в таком виде не рекомендуется, но можно
    # res = 0  # можно не указывать тип
    for item in params:
        res += item # склеивание строк
    return res

print(concatenatio(1, 2, 3, 4)) # 10 (1+2+3+4)

# рекурсия - функция, которая вызывает сама себя. 
# главное указать, в какой момент остановиться и перестать ее вызывать
# числа фибоначчи

def fib(n): # написали функцию, указали название и аргументы
    if n in [1, 2]: # логика выхода
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Кортежи - неизменяемый список

a = (3, 4) # кортеж
print(a)  # (3, 4)
print(a[0]) #  3
print(a[-1]) # 4 - последний элемент

# кортеж может состоять из большого количества координат
a = (3, 1, 41, 4)
print(a)
print(a[-2])
# присвоить элементу новое значение нельзя. кортеж - неизменяемый список.

t = ()
print(type(t))    # tuple (кортеж)

t = (1,)
print(type(t))   # tuple (кортеж)

t = (1)
print(type(t))   # int, кортеж с 1 аргументом не задают

t = (28, 9, 1990)
print(type(t))    # tuple (кортеж)

colors = ['red', 'green', 'blue']
print(colors)   # ['red', 'green', 'blue']

t = tuple(colors)
print(t)     # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10])  # IndexError: tuple index out of range
print(t[-2])  # green
# print(t[-200])  # IndexError: tuple index out of range

for e in t:
    print(e) # red green blue

a = (3, 4, 5)
print(a)  # (3, 4, 5)
print(a[0])  # 3

for item in a:
    print(item) # 3 4 5
# в рамках 1 кортежа можно миксовать разные данные: текст, цифры,

t = tuple(['red', 'green', 'blue']) #  можно распаковать кортеж в отдельные переменные
red, green, blue = t 
# можно прописать через запятую и присвоить значение переменной типа кортеж, 
# которая была определена на основе списка
# кортеж превращаем в список, а его в отдельные переменные
print('r:{} g:{} b:{}'.format(red, green, blue))  # r:red g:green b:blue







