# Складирование ноутбуков
from itertools import permutations as pmtt
x1, y1, z1 = int(input()), int(input()), int(input())
x2, y2, z2 = int(input()), int(input()), int(input())
b = [x2, y2, z2]
k = []
m = pmtt(b)
for i in m:
    k += [(x1//i[0])*(y1//i[1])*(z1//i[2])]
print(max(k))
