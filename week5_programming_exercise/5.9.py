# Больше предыдущего
s = str(input())
x = s.split(' ')
x = list(map(int, x))
m = []
for i in range(1, len(x)):
    if x[i] > x[i-1]:
        m += [x[i]]
for i in m:
    print(i, end=' ')
