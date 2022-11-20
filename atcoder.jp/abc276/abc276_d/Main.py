N=int(input())
A=list(map(int,input().split()))
a2=[0]*N
a3=[0]*N
for i in range(N):
  while A[i]%2==0 or A[i]%3==0:
    if A[i]%2==0:
      A[i]//=2
      a2[i]+=1
    else:
      A[i]//=3
      a3[i]+=1
if A.count(A[0])==N:
  ans=sum(a2)+sum(a3)-min(a2)*N-min(a3)*N
  print(ans)
else:
  print(-1)