import sys, string
num = input()
if num[0] == '+' or num[0] == '-' :
    num = num[1:]
if num[0] == '.' :
    for i in range(1,len(num)) :
        if not num[i].isdigit() :
            print('No')
            sys.exit()
else :
    i=0
    while  i<len(num) and num[i] != '.' :
        if not num[i].isdigit() :
            print('No')
            sys.exit()
        i += 1
    i += 1
    while i<len(num) :
        if not num[i].isdigit() :
            print('No')
            sys.exit()
        i += 1
print('Yes')
