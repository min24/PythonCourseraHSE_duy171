# Частотный анализ
import string
s = open('input.txt', 'r', encoding='utf8')
r = s.read()
s.close()
for i in string.whitespace:
    r = r.replace(i, ' ')
r = r.split()
d = dict()
for i in r:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
x = [(i, j) for i, j in zip(d.keys(), d.values())]
x = sorted(x, key=lambda i: (-i[1], i[0]))
for i in x:
    print(i[0])
