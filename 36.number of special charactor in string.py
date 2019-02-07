import sys, string
a = input()
b = 0
for i in a :
    if i.isalnum() or i.isspace() or i=='_': b += 1
print(len(a)-b)
