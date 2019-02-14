import sys, string
N,M=map(int,input().split())
diff=abs(N-M)
if diff%2==0:
	print("even")
else:
	print("odd")
