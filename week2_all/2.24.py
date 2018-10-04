# Упаковка *
l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
a1 = [l1+l2, max(w1, w2), max(h1, h2)]
a2 = [max(l1, l2), w1+w2, max(h1, h2)]
a3 = [max(l1, l2), max(w1, w2), h1+h2]
a4 = [l1+w2, max(l2, w1), max(h1, h2)]
a5 = [max(l1, w2), l2+w1, max(h1, h2)]
a6 = [max(l1, w2), max(l2, w1), h1+h2]
x = 0
for i in [a1, a2, a3, a4, a5, a6]:
    if i[0] <= lc and i[1] <= wc and i[2] <= hc:
        x += 1
if x == 0:
    print("NO")
else:
    print("YES")
