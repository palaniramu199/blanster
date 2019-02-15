import sys, string, math
s = input()
m = s.count(s[0])
flag = 1
for i in range(1,len(s)) :
    if s.count(s[i]) != m :
        flag = 0
        break
if flag :
    print('Yes')
else :
    print('No')
