import bisect
import sys
input = sys.stdin.readline
N=int(input())
A=list(int(input()) for _ in range(N))
ans=[0]
cnt=[0]
t=0
for i in range(N):
  j=0
  while A[i]%2==0:
    A[i]//=2
    j+=1
  ans.append(A[i])
  t+=2**j
  cnt.append(t)
for i in range(int(input())):
  ind=bisect.bisect_left(cnt,int(input()))
  print(ans[ind])