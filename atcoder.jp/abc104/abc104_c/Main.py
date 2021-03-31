D,G=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(D)]
ans=100000
for i in range(2**D):
  tmp=0
  cnt=0
  flg=0
  for j in range(D):
    if (i>>j)&1:
      tmp+=a[j][1]+a[j][0]*(j+1)*100
      cnt+=a[j][0]
    else:
      flg=j
  if tmp>=G:
    ans=min(ans,cnt)
  else:
    b=-(-((G-tmp)//100)//(flg+1))
    if b<a[flg][0]:
      ans=min(ans,cnt+b)
print(ans)