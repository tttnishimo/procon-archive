N=input()
L,R=map(int,input().split())
if len(N)==len(str(int(N))) and L<=int(N)<=R:
  print('Yes')
else:
  print('No')