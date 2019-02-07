num = int(input())
value = [1,1]
a,b = 1,1
if num==1 : print('1')
elif num==2 : print('1 1')
else :
    for i in range(2,num) :
        c = a+b
        value.append(c)
        a,b = b,c
    print(*value)
