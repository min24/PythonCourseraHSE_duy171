# Быстрое возведение в степень
a = float(input())
n = int(input())
if n % 2 == 0:
    print((a**2)**(n/2))
else:
    print(a*(a**2)**((n-1)/2))
