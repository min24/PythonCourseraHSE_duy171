# Сократите дробь
def ReduceFraction(n, m):
    import math
    x = math.gcd(n, m)
    return [n/x, m/x]
n = int(input())
m = int(input())
x = ReduceFraction(n, m)
print(int(x[0]), int(x[1]))
