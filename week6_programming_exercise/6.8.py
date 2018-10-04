# Проходной балл
x = open("input.txt", "r", encoding="utf8")
s = x.read()
x.close()
s = s.split('\n')
while '' in s:
    s.remove('')
k = int(s[0])
m = s[1:]
n = []
for i in m:
    n += [i.split()[-3:]]
n = list(map(lambda x: list(map(int, x)), n))
n = list(filter(lambda x: x[0] >= 40 and x[1] >= 40 and x[2] >= 40, n))
if len(n) <= k:
    print(0)
else:
    if k == 0:
        print(0)
    else:
        n = list(map(sum, n))
        if n.count(max(n)) > k:
            print(1)
        else:
            n = sorted(n, reverse=True)
            n1 = sorted(list(set(n)))[::-1]
            n2 = list(map(lambda x: len(n)-n[::-1].index(x), n1))
            n3 = []
            for i, j in zip(n2, n1):
                if i <= k:
                    n3 += [j]
            print(n3[-1])
