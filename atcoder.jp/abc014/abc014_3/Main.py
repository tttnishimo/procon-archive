import itertools
n=int(input())
a=[0]*(10**6+2)
for i in range(n):
  b,c=map(int,input().split())
  a[b]+=1
  a[c+1]-=1
a=list(itertools.accumulate(a))
print(max(a))