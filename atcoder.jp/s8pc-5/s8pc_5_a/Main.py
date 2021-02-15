n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=a[0]
for i in range(1,n):
  if ans>a[i]:
    ans=((ans-a[i])//t+1)*t+a[i]
  else:
    ans=a[i]
print(ans)