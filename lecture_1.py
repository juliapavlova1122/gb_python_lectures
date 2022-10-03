#  типы данных и переменная
#  int, float, boolean, str, list, None

from tkinter import Variable


value = None
a = 123
b = 1.23
# print(type(a))
# print(type(b))

# value = 12345
# print(type(value))

s = 'hello world'
print(s) # вывод строки
# ss = 'hello \'world'
# print(ss)

# sss = 'hello \nworld'
# print(sss) #\n с новой строки

print(a, '---', b, ' --- ',s)
print('{} - {} - {}'.format(a, b, s)) # формат
print(f'{a} - {b} - {s}') # интерполяция
print('{1} - {2} - {0}'.format(a, b, s))

f = True
print(f)

list = [1, 2, 3]
print(list)

list = ['1', '2', '3', 'hello', 4.5, True] # типы смешивать в списке можно, но не нужно
print(list)
# аккуратно с пробелами

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, '+', b, '=', a+b) # строки
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


print('Введите а');
a = float(input()) # int целые, float вещественные
print('Введите b');
b = float(input())
print(a, '+', b, '=', a+b) 
print('{} {}'.format(a, b))
print(f'{a} {b}')







