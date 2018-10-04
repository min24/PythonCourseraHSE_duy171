m = int(input())
a = map(int, str(input()).split())
n = int(input())
b = tuple(map(int, str(input()).split()))
c = tuple(sorted(b))
d = dict(zip(b, range(n)))


def median(x, y):
    return (y - x + 1)//2 + x

for k in a:
    if len(c) == 1:
        print(1, end=' ')
    else:
        t = len(c) - 1
        s = 0
        while t - s + 1 > 2:
            i = median(s, t)
            if k <= c[i]:
                s = s
                t = i
            else:
                s = i
                t = t
        if abs(c[s] - k) <= abs(c[t] - k):
            print(d[c[s]]+1, end=' ')
        else:
            print(d[c[t]]+1, end=' ')
