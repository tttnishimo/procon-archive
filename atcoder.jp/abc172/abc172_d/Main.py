n=int(input())
ans=0
for i in range(1,n+1):
  k=n//i
  ans+=i*(k+1)*k//2
print(ans)