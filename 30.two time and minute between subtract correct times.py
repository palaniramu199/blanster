import sys, string
hour1,minute1 = map(int,input().split())
hour2,minute2 = map(int,input().split())
difference = abs(hour1*60+minute1 - hour2*60-minute2)
print(difference//60,difference%60)
