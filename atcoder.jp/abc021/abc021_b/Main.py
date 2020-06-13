n=int(input())
a,b=map(int,input().split())
k=int(input())
c=list(map(int,input().split()))
flg=0
if k >= n-1:
  flg=1
if a in c or b in c:
  flg=1
if len(c)!=k:
  flg=1
for i in range(len(c)):
  for j in range(i+1,len(c)):
    if c[i]==c[j]:
      flg=1
if flg==0:
  print('YES')
else:
  print('NO')