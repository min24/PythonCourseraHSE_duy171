# Угадай число
n = int(input())
arr = input()
mno = set(range(1, n+1))
while arr != 'HELP':
    arr = set(map(int, arr.split()))
    ans = input()
    if ans == 'YES':
        mno.intersection_update(arr)
    elif ans == 'NO':
        mno.difference_update(arr)
    arr = input()
print(*sorted(list(mno)))
