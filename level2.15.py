a=input()
b=list(a)
dict = {i:b.count(i) for i in b}
maximum = max(dict, key=dict.get)  
print(maximum)
