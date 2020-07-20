n=int(input())
ans=[1,1,1]
for i in range(n):
  a=list(map(int,input().split()))
  a.sort()
  ans=[max(ans[j],a[j]) for j in range(3)]
print(ans[0]*ans[1]*ans[2])