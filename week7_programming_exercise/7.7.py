# Номер появления слова
import string
s = open('input.txt')
r = s.read()
s.close()
for i in string.whitespace:
    r = r.replace(i, ' ')
r = r.split()
d = dict()
for i in r:
    if i not in d:
        d[i] = 0
    else:
        d[i] = d[i] + 1
    print(d[i], end=' ')
