#no of digits
import sys
num = int(input('enter n : '))
sum = 0
value1 = num
while value1 > 0 :
    sum += 1
    value1 //= 10
print(sum)
