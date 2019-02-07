import sys, string
a = input()
b = 0
for c in a :
    if c.isalnum() or c.isspace() or c=='_': b += 1
print(len(a)-b)
