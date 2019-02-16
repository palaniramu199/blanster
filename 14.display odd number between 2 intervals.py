def main():
  a,b=map(int,input().split())
  for value in range(a+1,b+1):
    if(value%2!=0):
        print(value)
if __name__ == '__main__':
    main()
