import sys, string
num= input()
value = list(map(int,input().split()))
print(sum(value) // len(value))
