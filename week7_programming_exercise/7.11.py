# Выборы Президента
s = open('input.txt', 'r', encoding='utf8')
r = s.readlines()
s.close()
d = dict()
for i in r:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
x = [(i, j) for i, j in zip(d.keys(), d.values())]
x = sorted(x, key=lambda i: i[1], reverse=True)
m = sum(d.values())
if 2*x[0][1] > m:
    ans = [x[0][0]]
else:
    ans = [x[0][0], x[1][0]]
s = open('output.txt', 'w', encoding='utf8')
for i in ans:
    s.writelines(i)
