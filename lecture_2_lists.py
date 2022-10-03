# # списки сложнее

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e) # 1 2 3 4 5

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333 # меняя значения в 1 или 2 списке, они изменятся в обоих
# for e in list1:
#     print(e) # 123 333 3 4 5

# print()

# for e in list2:
#     print(e) # 123 333 3 4 5

# удаление последнего элемента

list1 = [1, 2, 3, 4, 5]
# print(len(list1))
# print(list1.pop()) # удаление последнего элемента
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.pop(2)) # удаление конкретного элемента
# print(list1)

print(list1.insert(2, 11)) # вставить элемент на позицию 2 (то есть 3)
print(list1) # [1, 2, 11, 3, 4, 5]

print(list1.append(22))  #  добавление в конец [1, 2, 11, 3, 4, 5, 22]
print(list1)






