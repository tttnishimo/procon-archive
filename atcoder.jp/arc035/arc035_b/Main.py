import itertools
n=int(input())
a=[int(input()) for _ in range(n)]
a.sort()
ans=a[0]
c=1
b=list(itertools.accumulate(a))
flg=1
for i in range(1,n):
  ans+=b[i]
  c*=flg
  c%=10**9+7
  if a[i]==a[i-1]:
    flg+=1
  else:
    flg=1
c*=flg
c%=10**9+7
print(ans)
print(c)