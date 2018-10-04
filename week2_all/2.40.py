# Числа Фибоначчи
def fibo(n):
    return int((1/(5**0.5))*(((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n))
n = int(input())
print(fibo(n))
