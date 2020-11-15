n,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[0]*10**6
for i in a:
  b[i[0]]+=i[2]
  b[i[1]]-=i[2]
flg=0
if b[0]>w:
  flg=1
for i in range(1,len(b)):
  b[i]+=b[i-1]
  if b[i]>w:
    flg=1
if flg==0:
  print('Yes')
else:
  print('No')