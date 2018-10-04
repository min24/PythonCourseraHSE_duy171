# Словарь синонимов
dict1 = dict()
dict2 = dict()
n = int(input())
for i in range(n):
    s = str(input()).split()
    dict1[s[0]] = s[1]
    dict2[s[1]] = s[0]
key = input()
if key in dict1:
    print(dict1[key])
elif key in dict2:
    print(dict2[key])
