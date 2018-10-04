# Максимум последовательности
now = int(input())
maxNow = now
while now != 0:
    now = int(input())
    if now > maxNow:
        maxNow = now
print(maxNow)
