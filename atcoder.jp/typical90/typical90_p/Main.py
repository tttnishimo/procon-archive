N=int(input())
a=list(map(int,input().split()))
a.sort()
ans=10**5
for i in range(N//a[2]+1):
  K=N-i*a[2]
  for j in range(K//a[1]+1):
    if (K-j*a[1])%a[0]==0:
      ans=min(ans,i+j+(K-j*a[1])//a[0])
print(ans)