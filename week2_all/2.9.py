# Коровы
n = int(input())
s = "{} korovy".format(n)
m = n % 10
if m == 1 and (n > 20 or n < 10):
    s = "{} korova".format(n)
elif (m in [0, 5, 6, 7, 8, 9]) or (n > 10 and n < 20):
    s = "{} korov".format(n)
print(s)
