N=int(input())
A=list(map(int,input().split()))
L=[i for i in range(2*10**5+1)]
ans=0
def dfs(v):
  if L[v]!=v:
    L[v]=dfs(L[v])
  return L[v]
for i in range(N//2):
  l=A[i]
  r=A[N-1-i]
  l=dfs(l)
  r=dfs(r)
  if l!=r:
    L[r]=l
    ans+=1
print(ans)