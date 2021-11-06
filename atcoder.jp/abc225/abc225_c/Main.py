N,M=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
  for j in range(M):
    if j==0 and i!=0:
      if B[i][0]!=B[i-1][0]+7:
        print('No')
        exit()
    elif j!=0:
      if B[i][j]!=B[i][j-1]+1 or (B[i][j]%7==1 and B[i][j-1]%7==0):
        print('No')
        exit()
print('Yes')