while True:
  n,k=map(int,input().split())
  if n==0 and k==0:
    break
  a=list(map(int,input().split()))
  a.sort()
  print(sum(a[:k]))
  