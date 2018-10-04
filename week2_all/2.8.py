# Шоколадка
n = int(input())
m = int(input())
k = int(input())
a = 'NO'
if ((k % n == 0) or (k % m == 0)) and k < m*n:
    a = "YES"
print(a)
