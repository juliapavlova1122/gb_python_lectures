# нахождение максимума из 2 чисел

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# if , elif

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# else:
#     print('Привет, ', username)


# Циклы. очень важны отступы

# собираем инвертированное число - полученное путем изменения порядка каждой цифры целого числа
# original = 235
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10 # Деление с остатком и присваивание (//=)
# print(inverted)

# a = 13 
# a //= 10
# print(a) # Деление с остатком и присваивание (//=)

# original = 235
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10 
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Цикл for

# for i in 1,2,3,4,5: 
# # i - счетчик, 1,2,3,4,5 - итерируемый объект
# # - это объект, который способен возвращать элементы по одному
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10) # выдает цифры от 1 до 10
# for i in r:
#     print(i)

# r = range(2, 5) # выдает цифры от 2 до 5
# for i in r:
#     print(i)

# r = range(1, 10, 2) # от 1 до 10 с шагом 2. Выдал нечетные
# for i in r:
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# О СТРОКАХ
# строка как массив символов

text = 'съешь еще этих мягких французских булок'

print(len(text)) # количество знаков
# help(len) - встроенная справка
# print('еще' in text) #39
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))
# for c in text:
#     print(c)
# print()
print(text[0]) # c - нахдится на 1 позиции
print(text[1]) # ъ
# print(text[len(text)]) # ошибка
print(text[len(text)-1]) # к
print(text[-5]) # 5 с конца - б
print(text[:]) # напечатать текст
print(text[0:2]) # текст от 0 символа до 2
print(text[len(text)-2:]) # 2 последние
print(text[2:8])
print(text[6:-18])
print(text[len(text)-2:])
print(text[0:len(text):6]) #сеикакл
print(text[::6]) #сеикакл
text = text[2:9] + text[-5] + text[:2]







