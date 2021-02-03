import itertools
n=int(input())
a=list(map(int,input().split()))
a=[0]+list(itertools.accumulate(a))
for i in range(1,n+1):
  print(max([a[j+i]-a[j] for j in range(n-i+1)]))