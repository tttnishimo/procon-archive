n,l=map(int,input().split())
s=[input() for _ in range(l)]
t=input()
t=t.index('o')
if n==1:
  print(1)
else:
  for i in range(l):
    if t==0:
      if s[-1-i][t+1]=='-':
        t+=2
    elif t==n*2-2:
      if s[-1-i][t-1]=='-':
        t-=2
    else:
      if s[-1-i][t+1]=='-':
        t+=2
      elif s[-1-i][t-1]=='-':
        t-=2
  print(t//2+1)