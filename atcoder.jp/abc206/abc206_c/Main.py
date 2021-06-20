import collections
N=int(input())
A=collections.Counter(list(map(int,input().split())))
ans=0
for i in A:
  N-=A[i]
  ans+=N*A[i]
print(ans)