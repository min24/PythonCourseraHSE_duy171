# Округление по российским правилам
x = float(input())
if x - round(x) == 0.5:
    print(round(x) + 1)
else:
    print(round(x))
