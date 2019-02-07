import sys, string
a = input()
b = a.count('.')
if a[-1] != '.' : b += 1
print(b)
