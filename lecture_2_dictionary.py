# Словари
# неупорядоченные коллекции произвольных обьектов с доступом по ключу

dictionary = {}
# обратный слэш ниже \ для того, чтобы писать не в одну строку, а каждый раз с новой. После него нельзя ставить пробел, коммент и тп
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary['up']) # замена значения в 3 строках кода
# dictionary['up'] = 'up' # замена значения
# print(dictionary['up'])  # замена значения

print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←

for k in dictionary.keys():
    print(k) # up left down right - ключи

for k in dictionary.values():
    print(k) # ↑ ← ↓ → - значения

for v in dictionary:
    print(dictionary[v]) # ↑ ← ↓ → - значения

print(dictionary['up'])  # ↑





