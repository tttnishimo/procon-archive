n=int(input())
a=[int(input()) for _ in range(n)]
a.sort()
t=a[0]
ans=1
for i in range(1,n):
  if t<a[i]:
    t+=a[i]
    ans+=1
print(ans)