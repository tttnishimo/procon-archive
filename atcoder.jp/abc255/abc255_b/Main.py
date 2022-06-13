N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[list(map(int,input().split())) for _ in range(N)]
t=0
for i in range(N):
  s=10**20
  for a in A:
    s=min(s,(B[i][0]-B[a-1][0])**2+(B[i][1]-B[a-1][1])**2)
  t=max(t,s)
print(t**.5)