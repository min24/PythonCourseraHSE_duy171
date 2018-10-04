# Котлеты *
k = int(input())
m = int(input())
n = int(input())
if n <= k:
    print(2*m)
elif n > k and n % k != 0 and 2*(n % k) <= k:
    print(int((2*m*((n-1)//k + 1)))-m)
elif n > k and n % k == 0:
    print(int(2*m*n/k))
else:
    print(int((2*m*((n-1)//k + 1))))
