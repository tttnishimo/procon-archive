import itertools
H,W=map(int,input().split())
s=[input() for _ in range(H)]
for i in itertools.product('LSR',repeat=H-1):
  t=s[H-1].index('s')
  flg=0
  for j in range(H-1):
    if i[j]=='L':
      t-=1
    elif i[j]=='R':
      t+=1
    if 0<=t<=W-1:
      if s[H-2-j][t]=='x':
        flg=1
    else:
      flg=1
  if flg==0:
    print(*i,sep='')
    exit()
print('impossible')