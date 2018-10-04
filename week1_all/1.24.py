# Проверка на делимость *
a = int(input())
b = int(input())
x = (a % b) == 0
print('YES'*x + 'NO'*(1-x))
