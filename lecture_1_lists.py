# Списки

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

ran = range(1, 6)
print(type(ran))  # <class 'range'>
numbers = list(ran)
print(type(numbers))   # <class 'list'>

print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2 #  в текущую переменную кладем новое значение, не в список
    print(i)  # 20 4 6 8 10
print(numbers) # в списке осталось как было [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('grey') # добавь в конец 
print(colors == ['red', 'green', 'blue', 'grey'])
colors.remove('red') # удалить элемент или так: 
# del colors[0]
print(colors)

