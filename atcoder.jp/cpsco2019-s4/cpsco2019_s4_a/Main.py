l,x=map(int,input().split())
x%=2*l
if x>l:
  print(l-(x-l))
else:
  print(x)