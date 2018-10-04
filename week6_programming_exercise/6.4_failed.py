# Гражданская оборона
import numpy as np
m = int(input())
a = tuple(map(int, str(input()).split()))
n = int(input())
b = tuple(map(int, str(input()).split()))
b = np.array(b)
for i in range(m):
    di = b-a[i]
    dis = tuple(map(abs, di))
    min_dis = min(dis)
    index_ = dis.index(min_dis)
    print(index_+1, end=' ')
