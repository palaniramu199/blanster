#median program
num = int(input())
value1 = list(map(int, input().split()))
value2 = sorted(value1)
a = len(value1) // 2
if len(value1)%2 == 1 :
    print(value2[a])
else :
    print((value2[a-1]+value1[a])/2)
