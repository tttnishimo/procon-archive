X,Y,Z=map(int,input().split())
for i in range(1,10000):
  if X*Y*Z==0:
    print(i)
    exit()
  X,Y,Z=Y-Z,Z-X,X-Y
print(-1)