n,k,m,r=map(int,input().split())
if n==1:
  print(r)
else:
  a=[int(input()) for _ in range(n-1)]
  a.sort(reverse=True)
  if sum(a[:k])>=k*r:
    print(0)
  else:
    a=k*r-sum(a[:k-1])
    if a>m:
      print(-1)
    elif a<=0:
      print(0)
    else:
      print(a)