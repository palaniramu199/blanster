#fAP
n,a,d = map(int, input().split())
total = a + (n-1)*d
value = n*(a+total)//2
print(value)
