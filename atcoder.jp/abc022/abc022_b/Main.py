n=int(input())
a={}
ans=0
for i in range(n):
  tmp=int(input())
  a[tmp]=a.get(tmp,0)+1
  if a[tmp] >= 2:
    ans += 1
print(ans)
  