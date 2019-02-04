N,A,D=input().split()
N,A,D=int(N),int(A),int(D)
value=0
total=0
while N>=0:
    total+=value
    value+=A
    N-=1
print(total)
