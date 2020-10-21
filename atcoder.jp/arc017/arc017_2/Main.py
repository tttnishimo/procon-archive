n,k=map(int,input().split())
ans=0
tmp=int(input())
flg=1
if flg>=k:
  ans+=1
for i in range(n-1):
  m=int(input())
  if tmp<m:
    flg+=1
  else:
    flg=1
  tmp=m
  if flg>=k:
    ans+=1
print(ans)