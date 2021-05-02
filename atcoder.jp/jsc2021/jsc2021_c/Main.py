A,B=map(int,input().split())
for i in range(B-A,0,-1):
  if B//i+(-A//i)>0:
    print(i)
    exit()