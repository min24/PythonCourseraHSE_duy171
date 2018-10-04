# Мороженое
k = int(input())
if k in [0, 1, 2, 4, 7]:
    print("NO")
else:
    print("YES")
# prove that every integer number x larger than 10 can be show by (3m + 5n)
"""
*case 1: x = 3k => m = k
*case 2: x = 3k + 1
         choose n = 2, m = k-3
         x = 3(k-3) + 5*2 = 3k + 1
*case 3: x = 3k + 2
         choose n = 1, m = k-1
"""
