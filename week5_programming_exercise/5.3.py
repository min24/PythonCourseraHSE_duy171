# Флаги
x1 = r'+___ '
x2 = '|{} / '
x3 = r'|__\ '
x4 = r'|    '
n = int(input())
print(x1*n)
for i in range(n):
    print(x2.format(i+1), end='')
print()
print(x3*n)
print(x4*n)
