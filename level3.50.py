a,b=map(int,input().split())
if b>a:
    print(0)
elif b==a:
    print(1)
else:
    sum=0
    while a>=b:
        sum+=1
        a=a-b
    print(sum)
    
