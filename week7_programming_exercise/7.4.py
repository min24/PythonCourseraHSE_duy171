# Количество слов в тексте
import sys
import string
r = sys.stdin.read()
r = str(r)
p = string.punctuation
w = string.whitespace
for i in w:
    r = r.replace(i, ' ')
print(len(set(r.split())))
