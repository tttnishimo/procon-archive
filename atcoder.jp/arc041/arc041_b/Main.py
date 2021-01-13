n,m=map(int,input().split())
b=[list(input()) for _ in range(n)]
b=[[int(b[i][j]) for j in range(m)] for i in range(n)]
a=[[0 for _ in range(m)] for _ in range(n)]
for i in range(1,n-1):
  for j in range(1,m-1):
    while b[i+1][j] and b[i-1][j] and b[i][j+1] and b[i][j-1]:
      b[i+1][j]-=1
      b[i-1][j]-=1
      b[i][j+1]-=1
      b[i][j-1]-=1
      a[i][j]+=1
for i in range(n):
  print(*a[i],sep='')