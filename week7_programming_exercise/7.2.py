# Пересечение множеств
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s1 = set(s1)
s2 = set(s2)
a = s1 & s2
a = sorted(list(a))
print(*a)
