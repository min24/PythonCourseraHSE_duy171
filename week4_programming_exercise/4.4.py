# Минимальный делитель числа
def MinDivisor(n):
    i = 1
    x = int(n**0.5)
    while i <= x:
        i += 1
        if n % i == 0:
            return i
    return n
n = int(input())
print(MinDivisor(n))
