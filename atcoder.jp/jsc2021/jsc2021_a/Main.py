X,Y,Z=map(int,input().split())
for i in range(10**6+1):
  if Y/X<=i/Z:
    print(i-1)
    exit()