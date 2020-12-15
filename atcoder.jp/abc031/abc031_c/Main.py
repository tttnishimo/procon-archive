n=int(input())
a=list(map(int,input().split()))
ans=-10000000
for i in range(n):
  ta=[]
  tb=[]
  for j in range(n):
    if i!=j:
      ta.append(sum(a[min(i,j):max(i,j)+1:2]))
      tb.append(sum(a[min(i,j)+1:max(i,j)+1:2]))
  ans=max(ans,ta[tb.index(max(tb))])
print(ans)