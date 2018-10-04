# Проверка числа на простоту
def ISPrime(n):
    i = 2
    x = int(n**0.5)
    while i <= x:
        if n % i == 0 and i < n:
            return False
        i += 1
    return True
n = int(input())
if ISPrime(n):
    print('YES')
else:
    print('NO')
