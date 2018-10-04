# Полиглоты
st = int(input())
x = []
for i in range(st):
    st1 = int(input())
    x1 = []
    for j in range(st1):
        x1 += [str(input())]
    x += [x1]
s = []
for i in x:
    s += i
s = set(s)
t = set(s)
for i in x:
    i = set(i)
    s.intersection_update(i)
print(len(s))
s = sorted(list(s))
for i in s:
    print(i)
print(len(t))
t = sorted(list(t))
for i in t:
    print(i)
