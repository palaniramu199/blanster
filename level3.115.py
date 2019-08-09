n=int(input())
a=[2,3,5,7]
for i in range(2,n):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
        continue
    if i%2==1 or i%3==1 or i%5==1 or i%7==1 or i%9==1:
        a.append(i)
sum=0
for i in range(0,len(a)):
    #print(i)
    for j in range(i,len(a)):
        #print(j)
        if a[i]+a[j]==n:
            sum+=1
print(sum)
