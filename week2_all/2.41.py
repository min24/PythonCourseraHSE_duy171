# Номер числа Фибоначчи
def fibo(n):
    return int((1/(5**0.5))*(((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n))
n = int(input())
i = 0
while fibo(i) < n:
    i += 1
if fibo(i) == n:
    print(i)
else:
    print(-1)
