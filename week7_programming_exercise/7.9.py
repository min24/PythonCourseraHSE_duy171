# Самое частое слово
import string
import sys
s = sys.stdin.read()
for i in string.whitespace:
    s = s.replace(i, ' ')
s = s.split()
d = dict()
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
m = max(d.values())
x = []
for i in d:
    if d[i] == m:
        x += [i]
x = sorted(x)
print(x[0])
