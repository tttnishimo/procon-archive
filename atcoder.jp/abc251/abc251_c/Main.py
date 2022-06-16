N=int(input())
A=[list(map(str,input().split())) for _ in range(N)]
s=set()
ans=[0,0]
for i in range(N):
  if A[i][0] not in s:
    s.add(A[i][0])
    if ans[1]<int(A[i][1]):
      ans[0]=i+1
      ans[1]=int(A[i][1])
print(ans[0])