N=int(input())
A=list(map(int,input().split()))
A.sort()
ave=sum(A)/N
t=ave-A[0]/2
ans=t
for i in range(1,N):
  t+=(A[i]-A[i-1])*(-0.5+i/N)
  ans=min(ans,t)
print(ans)