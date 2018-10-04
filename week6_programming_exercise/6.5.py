# Отсортировать список участников по алфавиту
s = open('input.txt', 'r', encoding='utf8')
t = s.readlines()
x = []
s.close()
for i in t:
    x += [i.split()]
k = []
for i in x:
    k += [[i[0]] + [i[1]] + [i[-1]]]
k = list(sorted(k, key=lambda x: x[0]))
for i in k:
    print(' '.join(i))
