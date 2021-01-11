import itertools
import bisect
n=int(input())
p=0
q=[]
for i in range(n):
  a,b=map(int,input().split())
  p+=a
  q.append(2*a+b)
q.sort(reverse=True)
q=list(itertools.accumulate(q))
print(bisect.bisect_right(q,p)+1)