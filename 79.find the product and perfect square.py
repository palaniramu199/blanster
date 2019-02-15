import sys, string, math
a,b = map(int,input().split())
N = math.sqrt(a * b)

if N == int(N) : 
	print('yes')
else :           
	print('no')
