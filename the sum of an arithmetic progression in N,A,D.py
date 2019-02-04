#N,A,D=input().split()
#N,A,D=int(N),int(A),int(D)
N,A,D=5,1,0
value=0
total=0
while A>=0:
    total+=value
    value+=N
    A-=1
print(total)
