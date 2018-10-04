# Последний максимум
s = str(input())
x = s.split()
y = list(map(int, x))
m = max(y)
z = y[::-1]
n = z.index(m)
n = len(y)-1-n
print(m, n)
