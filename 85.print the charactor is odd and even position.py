import sys, string, math
n = input()
n1 = ''
n2 = ''
for i in range(len(n)) :
    if i%2 == 0 : n1 += n[i]
    else :        n2 += n[i]
print(n1,n2)
