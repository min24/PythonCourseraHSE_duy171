# Разворот последовательности
def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
print(0)
rec()
