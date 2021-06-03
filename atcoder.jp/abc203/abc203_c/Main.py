N,K=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort()
for i in A:
  if i[0]<=K:
    K+=i[1]
print(K)