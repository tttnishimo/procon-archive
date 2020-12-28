n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
t=0
for i in range(n):
  t+=a[i]
  if t>=m:
    print(i+1)
    break