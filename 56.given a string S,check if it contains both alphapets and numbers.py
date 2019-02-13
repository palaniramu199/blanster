import sys, string
str = input()
alpha,num = 0,0
for c in str :
    if c.isalpha() : alpha += 1
    if c.isdigit() : num += 1
if alpha and num : print('Yes')
else :       print('No')

