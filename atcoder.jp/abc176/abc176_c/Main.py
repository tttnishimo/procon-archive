n=int(input())
a=list(map(int,input().split()))
ans=0
tmp=a[0]
for i in a:
  if tmp>i:
    ans+=tmp-i
  else:
    tmp=i
print(ans)