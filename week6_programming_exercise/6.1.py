# Слияние списков
def merge(a, b):
    c = []
    i, j = 0, 0
    for k in range(len(a)+len(b)):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                c += [a[i]]
                i += 1
            elif a[i] == b[j]:
                c += [a[i]] + [b[j]]
                i += 1
                j += 1
            else:
                c += [b[j]]
                j += 1
        elif i < len(a):
            c += [a[i]]
            i += 1
        elif j < len(b):
            c += [b[j]]
            j += 1
    return c
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in merge(x, y):
    print(i, end=' ')
