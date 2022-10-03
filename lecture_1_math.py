# арифметические операции
# +, -, *, /, %, //, **
# **, 

a = 3
b = 3

# c = a // b # деление в целых числах
# с = a % b # остаток от деления
# c = a**b # степень
# c = round(a * b, 3) # округление
# a +=5 # вместо a = a + 5
print(a)


# логические операции
# >, >=, <, <=, ==, !=
# not, and, or. is, is not, in, not in

# a = 1 > 4
# print(a) - # результат False
# a = 1 != 4
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a==b) # True

# a = [1,2]
# b = [1,2]
# print(a==b) # True

# a = 1 < 3 < 5 # тройные неравенства
# print(a) # True

# a = 1
# b = 4
# x = 2
# print(a<b>x) # True

# f = 1 > 2 or 4 < 6
# print(f) # True - дизьюнкция

# f = [1,2,3,4]
# print(not 2 in f)  # false

# f = [1,2,3,4]
# is_odd = f[0] % 2 == 0
# print(is_odd) # False (1 - нечетное)

# f = [1,2,3,4]
# is_odd = not f[0] % 2 
# print(is_odd) # False - то же самое

f = [1,2,3,4]
print(f) 
print(not 2 in f)  

is_odd = not f[0] % 2 
print(is_odd)


