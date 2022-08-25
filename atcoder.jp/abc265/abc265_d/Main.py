import itertools
import bisect
N,P,Q,R=map(int,input().split())
A=[0]+list(map(int,input().split()))
a=set(itertools.accumulate(A))
for i in a:
  if i+P in a:
    if i+P+Q in a:
      if i+P+Q+R in a:
        print('Yes')
        exit()
print('No')