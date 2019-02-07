import sys, string
num = int(input())
value = bin(num)[2:]
if value.count('1') == 1 : print('yes')
else :                 print('no')

