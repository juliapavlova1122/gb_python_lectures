# множества

colors = {'red', 'green', 'blue'} # кладем значения в некоторую переменную - это множество
print(type(colors))  # set
print(colors) # {'red', 'blue', 'green'}

colors.add('red') # добавить элемент во множество, в данном случае элемент уже был и ничего не добавилось
colors.add('grey') # добавить новый элемент во множество
print(colors) # {'red', 'grey', 'green', 'blue'}
colors.remove('red') # удаление элемента, выдаст ошибку на удаление несуществующего элемента
print(colors) 
colors.discard('red') # ok. тоже сброс элемента
print(colors)  # {'blue', 'grey', 'green'}
colors.clear()  # {} - очистить множество и дальше можно работать с пустым множеством
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # {1, 2, 3, 5, 8} - множество на основе имеющегося
print(c)
u = a.union(b) # объединение множеств - вызываем первое, 
# в качестве аргумента второе - {1, 2, 3, 5, 8, 13, 21}
print(u)
i = a.intersection(b) # пересечение  {8, 2, 5}
print(i)
dl = a.difference(b) # разность множеств {1, 3}
print(dl)
dr = b.difference(a) # {13, 21}
print(dr)

q = a\
    .union(b) \
    .difference(a.intersection(b))
print(q)  # {1, 21, 3, 13}

s = frozenset(a) # замороженное множество (неизменяемое), удаление и тп работать не будут

