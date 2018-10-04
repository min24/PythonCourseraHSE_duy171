# Удаление фрагмента
s = str(input())
x = s.find('h')
y = s.rfind('h')
z = s[:x] + s[y+1:]
print(z)
