# Гражданская оборона
import time
time_start = time.time()
m = 10
a = list(map(int, str("79 64 13 8 38 29 58 20 56 17").split()))
n = 10
b = tuple(map(int, str("53 19 20 85 82 39 58 46 51 69").split()))
c = sorted(b)


def median(x, y):
    return (y - x + 1)//2 + x


def nearest(k, x):
    if len(x) == 1:
        return x[0]
    t = len(x) - 1
    s = 0
    while t - s + 1 > 2:
        i = median(s, t)
        if k <= x[i]:
            s = s
            t = i
        else:
            s = i
            t = t
    if abs(x[s] - k) <= abs(x[t] - k):
        return x[s]
    else:
        return x[t]
for i in a:
    print(b.index(nearest(i, c))+1, end=' ')
time_end = time.time()
print(time_end - time_start)