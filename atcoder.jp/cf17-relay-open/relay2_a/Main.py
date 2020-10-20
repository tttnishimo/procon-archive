k,a,b=map(int,input().split())
if a>=k:
  print(1)
elif b>=a:
  print(-1)
else:
  if (k-a)%(a-b)==0:
    print((k-a)//(a-b)*2+1)
  else:
    print((k-a)//(a-b)*2+3)